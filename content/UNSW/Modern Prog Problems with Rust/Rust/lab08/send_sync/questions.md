1) I saw someone's code fail to compile because they 
were trying to send non-thread-safe data across threads. 
How does the Rust language allow for static (i.e. at compile time)
guarantees that specific data can be sent/shared acrosss threads?

Rust enforces thread safety *statically* through two marker traits: **`Send`** and **`Sync`**.  
These traits are automatically checked by the compiler to ensure that only thread-safe data is transferred or shared across threads.

- **`Send`** — indicates that ownership of a value can be safely transferred to another thread.  
- **`Sync`** — indicates that references to a value can be safely shared between threads.

At compile time, Rust verifies that any type moved or referenced across thread boundaries implements these traits.  
If not, the compiler raises an error — preventing potential *data races* and *undefined behaviour* before the program even runs.

2) Do you have to then implement the Send and Sync traits for 
every piece of data (i.e. a struct) you want to share and send across threads?

No.  
In most cases, you **do not implement** these traits yourself — the compiler automatically derives them when all fields of your type are `Send` or `Sync`.

For example:

```rust
struct MyData {
    value: i32, // i32 is Send + Sync
}
// MyData automatically becomes Send + Sync
```
Manual implementation is almost never required and usually unsafe, because the compiler cannot automatically verify correctness.

3) What types in the course have I seen that aren't Send? Give one example, 
and explain why that type isn't Send 
A common example is **`Rc<T>`** (non-atomic reference counting).  
`Rc<T>` is **not `Send`** because it uses **non-atomic reference counters**, which can be modified by multiple threads simultaneously if shared — leading to race conditions.

If you need thread-safe reference counting, you must use **`Arc<T>`**, which uses atomic operations and is both `Send` and `Sync`.

```rust
// ❌ Not Send or Sync
use std::rc::Rc;
let rc = Rc::new(5);

// ✅ Thread-safe version
use std::sync::Arc;
let arc = Arc::new(5);
```

4) What is the relationship between Send and Sync? Does this relate
to Rust's Ownership system somehow?

Yes — both traits are tightly connected to Rust’s **ownership and borrowing model**.

- `Send` ensures that **ownership transfer** between threads is safe.  
  (A value can only have one owner at a time.)
- `Sync` ensures that **shared references (`&T`)** can be safely accessed by multiple threads concurrently.  

Formally, if a type `T` is `Sync`, then `&T` is `Send`.

Rust’s ownership system already prevents aliasing and ensures exclusive access (`&mut T`), so `Send` and `Sync` simply extend those guarantees to multi-threaded contexts.

5) Are there any types that could be Send but NOT Sync? Is that even possible?

Yes, it is possible.

Example: **`MutexGuard<T>`** (the temporary lock guard returned by `Mutex::lock()`).

- It is `Send` because the guard (which owns the lock) can be moved to another thread.  
- But it is **not `Sync`**, because multiple threads must not hold references to the same guard simultaneously — that would violate mutual exclusion.

So `Send` but not `Sync` types exist when *ownership transfer* is safe, but *shared access* is not.

6) Could we implement Send ourselves using safe rust? why/why not?

No — you cannot safely implement `Send` (or `Sync`) manually using **safe Rust**.

Implementing these traits is marked `unsafe` for a reason:

```rust
unsafe impl Send for MyType {}
```

This is because the compiler cannot automatically verify the thread-safety guarantees for your type.
A wrong implementation could cause data races, which violate Rust’s core safety guarantees.

In safe Rust, you rely on the compiler’s automatic derivation; only low-level system libraries might need to manually (and very carefully) implement these traits using unsafe.