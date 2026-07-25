---
tags:
  - UNSW
  - UNSW/COMP6991
  - Topic/Rust
---

# Question 1

## Q1.1 (2 marks)

A C programmer who is starting to learn Rust has asked: "Aren't match statements just complicated if statements?". Give a specific example of a situation where you believe a match statement would significantly improve code quality, instead of a series of if/else statements.

> [!note] Answer 
> ### ✅ Final Short Version (if answer must be short)
> 
> A `match` statement is not just a complex `if`.  
> For example, when matching over an enum:
> 
> ```rust
> match msg {
>     Message::Ping        => println!("ping"),
>     Message::Pong        => println!("pong"),
>     Message::Data(s)     => println!("data = {}", s),
>     Message::Error(code) => println!("error = {}", code),
> }
> ```
> 
> This is clearer, safer, and more readable than a long chain of `if/else`.  
> Rust also enforces **exhaustiveness**, preventing missing cases—something `if/else` cannot do.  
> Thus, `match` significantly improves code quality whenever you must handle many exclusive patterns, especially enums.
> 

## Q1.2 (2 marks)

The following Rust code fails to compile, but equivalent code in other popular programming languages (e.g. C, Java, Python) compiles and/or works correctly. Explain what issue(s) prevent the Rust compiler from building this code, and the philosophy behind this language decision.

struct Coordinate {
    x: i32,
    y: i32,
};
let coord1 = Coordinate {x: 1, y: 2};
let coord2 = coord1;
let coord_sum = Coordinate { x: coord1.x + coord2.x, y: coord1.y + coord2.y };

> [!NOTE] Answer
> ### ✅ **Model Answer (Concise + Exam-Ready)**
> 
> Rust rejects this code because **moving `coord1` into `coord2` invalidates `coord1`**, and afterwards the code attempts to read fields from `coord1`.  
> In Rust, a struct does **not** implicitly copy its data unless it implements `Copy`.  
> Thus:
> 
> ```rust
> let coord2 = coord1;   // coord1 is moved here
> coord1.x               // ❌ coord1 no longer valid
> ```
> 
> In languages like C, Java, or Python, values are copied or references are used automatically, so this pattern works.  
> Rust intentionally prevents such implicit copies to avoid accidental data duplication, aliasing bugs, or use-after-free errors.  
> This reflects Rust’s philosophy of **explicit ownership and moves**, ensuring memory-safe code without a garbage collector.
> 
> 

## Q1.3 (3 marks)

In other languages, the operation: `"first_string" + "second_string"` produces a new string, `"first_stringsecond_string"`. This particular operation **does not** work in Rust.

1. Why does Rust not implement this operation on the `&str` type?
2. Would it be possible for the Rust language developers to implement this? What rust feature would they use to implement it?
3. Do you think the Rust language developers should implement this operation? Give one reason to justify your answer.

> [!NOTE] Answer
> ### ✅ **Model Answer (Concise + Exam-Ready)**
> 
> ##### **1. Why does Rust not implement `"a" + "b"` for `&str`?**
> 
> Because `&str` is a **borrowed, immutable slice**, and has **no ownership** over its data.  
> Concatenation requires allocating a **new owned string**, but `&str` cannot allocate or modify memory, so Rust deliberately avoids providing `+` for borrowed string slices.
> 
> ---
> 
> #### **2. Could Rust developers implement this? What feature would they use?**
> 
> Yes, they _could_. They would implement it using a **trait**, specifically:
> 
> ```rust
> impl Add<&str> for &str { ... }
> ```
> 
> i.e., adding an implementation of the `Add` trait for `&str`.  
> The language does not forbid it; it is simply not provided.
> 
> ---
> 
> #### **3. Should Rust implement this operation? Why or why not?**
> 
> Probably **no**.  
> Allowing `&str + &str` would implicitly allocate a new `String`, which hides a heap allocation and goes against Rust’s philosophy of **explicit, predictable costs**.  
> Rust prefers:
> 
> ```rust
> String + &str
> ```
> 
> where the need for allocation is clear from the use of an owned `String`.
> 

## Q1.4 (3 marks)
Rust beginners have posted some questions on a programming forum:

1. How can I turn an owned value into a shared borrow?
2. How can I turn a shared borrow into an exclusive borrow!
3. Why am I allowed to turn an exclusive borrow into a shared borrow?

Provide a short answer to each question. Importantly, note that some questions might ask for something that is not possible (in which case, you should say so and explain why).

> [!NOTE] Answer
> ### ✅ **Model Answer (Concise + Exam-Ready)**
> 
> #### **1. How can I turn an owned value into a shared borrow?**
> 
> This is always allowed.  
> You simply take a reference:
> 
> ```rust
> let s = String::new();
> let r: &String = &s;
> ```
> 
> Rust lets you create immutable borrows (`&T`) from owned values because the owner guarantees the data remains valid.
> 
> ---
> 
> #### **2. How can I turn a shared borrow into an exclusive borrow?**
> 
> You **cannot** do this.  
> A shared borrow (`&T`) means other readers may exist, so Rust cannot safely give you a mutable/exclusive borrow (`&mut T`).  
> Allowing this would violate Rust’s aliasing rules and could cause data races or undefined behaviour.
> 
> ---
> 
> #### **3. Why am I allowed to turn an exclusive borrow into a shared borrow?**
> 
> This **is allowed**, because if you hold an exclusive borrow (`&mut T`), the compiler guarantees that **you are the only reference**.  
> Since no other references exist, it is always safe to create a shared borrow (`&T`) from it.
> 
> ---

# Question 4
## Q4.1 (2 marks)

Steve is writing some Rust code for a generic data structure, and creates a (simplified) overall design alike the following:
```Rust
struct S {
    // some fields...
}
impl S {
    fn my_func<T>(value: T) {        todo!()
    }
}
```

He soon finds that this design is not sufficient to model his data structure, and revises the design as such:
```Rust
struct S<T> {
    // some fields...
}
impl<T> S<T> {
    fn my_func(value: T) {        todo!()
    }
}
```

Give an example of a data-structure that Steve could be trying to implement, such that his first design would not be sufficient, and instead his second design would be required for a correct implementation. Furthermore, explain why this is the case.

> [!NOTE] Answer
> ### ✅ **Model Answer (Concise + Exam-Ready)**
> 
> A simple example is a **generic container**, such as a stack:
> 
> ```rust
> struct Stack<T> {
>     items: Vec<T>,
> }
> 
> impl<T> Stack<T> {
>     fn push(&mut self, value: T) { … }
> }
> ```
> 
> This data structure _must_ store values of type `T` **inside the struct itself**.  
> Therefore, the type parameter `T` must be attached to the struct:
> 
> - The first design
>     
>     ```rust
>     struct S { … }
>     impl S {
>         fn my_func<T>(value: T) { … }
>     }
>     ```
>     
>     only makes the _method_ generic, meaning the struct `S` cannot store or track elements of type `T`.
>     
> - The second design
>     
>     ```rust
>     struct S<T> { … }
>     impl<T> S<T> { … }
>     ```
>     
>     makes the _entire struct_ generic, allowing instances of `S<T>` to own data of type `T`.
>     
> 
> Thus, for any data structure that stores generic values (e.g., `Vec`, `Stack<T>`, `Queue<T>`, `LinkedList<T>`), Steve’s first design is insufficient because the struct cannot hold values of type `T`. The second design is required because the type parameter must apply to the data stored inside the structure itself.
> 

## Q4.2 (3 marks)
Emily is designing a function that has different possibilities for the value it may return. She is currently deciding what kind of type she should use to represent this property of her function.

She has narrowed down three possible options:

1. An enum
2. A trait object
3. A generic type (as `fn foo(...) -> impl Trait`)

For each of her possible options, explain one possible advantage and one possible disadvantage of that particular choice.

> [!NOTE] Answer
> ### ✅ **Model Answer (Concise + Exam-Ready)**
> 
> #### **1. Using an enum**
> 
> **Advantage:**
> 
> - All possible return variants are known at compile time, so the compiler can enforce exhaustiveness and enable efficient, static dispatch.
>     
> 
> **Disadvantage:**
> 
> - All variants must be listed ahead of time; cannot extend with new variants without modifying the enum definition (closed set).
>     
> 
> ---
> #### **2. Using a trait object (e.g., `Box<dyn Trait>`)**
> 
> **Advantage:**
> 
> - Allows returning different concrete types unknown until runtime, and supports dynamic extensibility without modifying existing code.
>     
> 
> **Disadvantage:**
> 
> - Requires heap allocation and dynamic dispatch (`dyn`), which has runtime cost and loses compile-time optimizations.
>     
> 
> ---
> 
> #### **3. Using a generic return type (`-> impl Trait`)**
> 
> **Advantage:**
> 
> - Zero-cost abstraction: the compiler knows the concrete type, enabling inlining and static dispatch, without exposing the actual type.
>     
> 
> **Disadvantage:**
> 
> - Only one concrete return type per function; cannot return different implementors of the trait depending on runtime conditions.

## Q4.3 (5 marks)

Rust's macro system offers an extremely flexible method for code generation and transfiguring syntax, but this language feature comes with certain costs. Identify 3 downsides to the inclusion, design, or implementation of Rust's macro system.

(Note that your downsides may span any amount and combination of the categories above. e.g. you could write all 3 on just one category, or one on each, or anything in-between.)

> [!NOTE] Answer
> ### ✅ **Model Answer (Concise + Exam-Ready)**
> 
> #### **1. Macros harm readability and error messages**
> 
> Rust macros operate on raw token streams before type checking.  
> This often leads to **obscure compiler errors**, poor diagnostics, and code that is harder to read because the actual executed code is not written explicitly.
> 
> ---
> 
> #### **2. Macros complicate the compiler and language design**
> 
> Rust must support both hygienic macros (`macro_rules!`) and procedural macros, which significantly increases **compiler complexity**, slows compile times, and makes the language harder to evolve without breaking existing macro behavior.
> 
> ---
> ## **3. Macros reduce IDE support and tooling quality**
>
Because macro-generated code is created before semantic analysis, editors struggle with **code navigation, autocompletion, refactoring, and static analysis** inside macro-expanded regions, harming developer experience.
>
> ---
> Rust macros are powerful but come with drawbacks: worse readability and error messages, increased compiler complexity, and weaker tooling/IDE support due to code generation happening before type checking.

# Question 5
## Q5.1 (3 marks)
In many other popular programming languages, mutexes provide `lock()` and `unlock()` methods which generally do not return any value (i.e. `void`).

What issues could this cause?
How does Rust differently implement the interface of a `Mutex`, and what potential problems does that help solve

> [!NOTE] Answer
> **Issues in languages where `lock()`/`unlock()` return void:**
> 
> 1. _Forgetting to call `unlock()`_ (e.g., early return / exception) → causes deadlock.
>     
> 2. _Unlocking the wrong mutex or unlocking without owning it_ (no compile-time checking).
>     
> 3. _Accessing shared data without holding the lock_ (language cannot enforce correctness).
>     
> 
> **Rust’s approach:**  
> Rust’s `Mutex::lock()` returns a **MutexGuard**, and the lock is released when the guard is dropped (RAII).
> 
> - Prevents forgetting to unlock (automatic release).
>     
> - Prevents unlocking the wrong mutex (no manual `unlock()` API).
>     
> - Ensures shared data can only be accessed via the guard, guaranteeing it is always accessed under the lock.

## Q5.2 (2 marks)
In Rust, locking a `Mutex` returns a `Result`, instead of simply a `MutexGuard`. Explain what utility this provides, and why a programmer might find this important.

> [!NOTE] Answer
> **Why `lock()` returns a `Result`:**
> 
> - If the holding thread panics, the mutex becomes **poisoned**. `lock()` then returns `Err(PoisonError)` instead of silently giving a potentially inconsistent value.
>     
> 
> **Utility / importance to programmers:**
> 
> - Allows the programmer to **detect and handle** poisoned locks (decide to abort, retry, or recover data).
>     
> - Prevents silently continuing with corrupted shared state, improving **safety and correctness** in concurrent programs.

## Q5.3 (3 marks)
While reviewing someone's code, you find the following type: `Box<dyn Fn() -> i32 + Send>`.

Explain what the `+ Send` means in the code above?

Explain one reason you might need to mark a type as `Send`, and what restrictions apply when writing a closure that must be `Send`.

> [!NOTE] Answer
> ### **What does `+ Send` mean?**
> 
> `Box<dyn Fn() -> i32 + Send>` means the trait object must implement **Send**,  
> i.e. the closure can be **safely transferred to another thread**.
> 
> ---
> 
> ### **Why might you need a type to be `Send`?**
> 
> When sending the closure to another thread (e.g., via `std::thread::spawn` or a channel), Rust requires the value to implement `Send`.  
> Marks that the value can be moved across thread boundaries **without data races**.
> 
> ---
> 
> ### **What restrictions apply to a `Send` closure?**
> 
> A closure is `Send` only if **all captured variables are also `Send`**.  
> Thus it **cannot capture non-Send types** (e.g., `Rc<T>`, raw pointers, etc.),  
> and must only capture data that is safe to move to another thread.

## Q5.4 (2 marks)

Your friend tells you they don't need the standard library's channels, since they've implemented their own alternative with the following code:
```Rust
use std::collections::VecDeque;
use std::sync::Mutex;
use std::sync::Arc;
use std::thread;
#[derive(Clone, Debug)]
struct MyChannel<T> {
    internals: Arc<Mutex<VecDeque<T>>>
}
impl<T> MyChannel<T> {
    fn new() -> MyChannel<T> {
        MyChannel {            internals: Arc::new(Mutex::new(VecDeque::new()))
        }    }    fn send(&mut self, value: T) {        let mut internals = self.internals.lock().unwrap();
        internals.push_front(value);
    }
    fn try_recv(&mut self) -> Option<T> {
        let mut internals = self.internals.lock().unwrap();
        internals.pop_back()
    }
}
fn main() {
    let mut sender = MyChannel::<i32>::new();
    let mut receiver = sender.clone();
    sender.send(5);
    thread::spawn(move || {
        println!("{:?}", receiver.try_recv())
    }).join().unwrap();
}
```

Identify a use-case where this implementation would not be sufficient, but the standard library's channel would be.

Furthermore, explain why this is the case.
# Question 7

# Question 8

