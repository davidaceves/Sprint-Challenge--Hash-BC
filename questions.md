## Interview Questions

1. What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
    The runtime complexity to access an array is O(1). Adding or removing to the front of an array is O(n) because you need to shift the entire array over by one, for the back it is O(1) because the array does not require a shift.

2. What is the worse case scenario if you try to extend the storage size of a dynamic array?
    Every time you have to extend the storage you are mostly going to be doubling the size of the array. This makes the append an O(n) operations vs O(1).

3. Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
    Blockchain is made up a genesis block followed by interconnected blocks, the blocks are all connected by hashes. The blocks allow for secure transfer of data with an excellent history of transactions made stored on all machines
    
4. Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
    A proof of work function adds computational work to create a new block in the chain. This protects the chain from attack because in order for the attacker to change the history of a block they would need to redo all proofs and have the longest chain before anyone else. Another possible attack is if someone takes control of 51% of the global computing power allowing them to rewrite blockchain history.