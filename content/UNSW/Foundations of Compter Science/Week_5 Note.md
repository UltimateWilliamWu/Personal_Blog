---
tags:
  - LectureNotes
---
## 1. Propositions
A **proposition (or sentence)** is a declarative statement; something that is either true or false.
Logical connectives join together propositions to build larger, compound propositions.
![[Pasted image 20241114141846.png]]
## 2. Tautologies, Contradictions and Contingencies
>[!note] Definition
>A proposition is: 
>- a tautology if it is always true, 
>- a contradiction if it is always false, 
>- a contingency if it is neither a tautology or a contradiction, 
>- satisfiable if it is not a contradiction.
## 3. Logical equivalence
>[!note] Definition
>Two propositions are logically equivalent if they are true for the same truth values of their atomic propositions.
## 4. Entailment and Validity
An argument consists of a set of propositions called premises and a declarative sentence called the conclusion.
An argument is valid if the conclusions are true whenever all the premises are true. Thus: if we believe the premises, we should also believe the conclusion. (Note: we don’t care what happens when one of the premises is false.)
## 5. Syntax & Semantics
The first step in the formal definition of logic is the separation of syntax and semantics
### Syntax
>[!important] Well-formed formulas
>Let Prop = {p, q, r , . . .} be a set of propositional letters. Consider the alphabet
>$$Σ = Prop ∪ \{ ⊤, ⊥, ¬, ∧, ∨, →, ↔, (, ) \}.$$

>[!note] Conventions
>To aid readability some conventions and binding rules can and will be used not in proof assistant. 
>- Parentheses omitted if there is no ambiguity (e.g. p ∧ q) 
>- ¬ binds more tightly than ∧ and ∨, which bind more tightly than → and ↔ (e.g. p ∧ q → r instead of ((p ∧ q) → r ) 
>- ∧ and ∨ associate to the left: p ∨ q ∨ r instead of ((p ∨ q) ∨ r )
### Semantics
>[!important] Boolean Algebras
>![[Pasted image 20241114155325.png]]
## 6. Satisfiability, Validity and Equivalence
A formula φ is 
- satisfiable if v (φ) = true for some truth assignment v (v satisfies φ) 
- a tautology if v (φ) = true for all truth assignments v 
- unsatisfiable or a contradiction if v (φ) = false for all truth assignments v
## 7. Logical equivalence
>[!note] Definition
>Two formulas, φ and ψ, are logically equivalent, φ ≡ ψ, if v (φ) = v (ψ) for all truth assignments v .
>>[!important] Fact
>>φ ≡ ψ if, and only if, (φ ↔ ψ) is a tautology.
## 8. The Master Theorem
>[!warning] Theorem
>![[Pasted image 20241114163214.png]]

>[!note] Notice
>The Master Theorem applies to recurrences where T (n) is defined in terms of T (n/b); not in terms of T (n − 1).
