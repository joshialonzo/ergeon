Describe in your own words what is GIL in python, and the pros and cons of it.

Answer:

* Definition: The Global Interpreter Lock is a mechanism to allow the execution of only one thread at a time.
* Advantages: The pros are that it prevents race conditions and simplifies memory management. It can be used for IO-bound tasks like file and network operations. This can be useful in automation scenarios where we integrate several services and try to delegate work to them. These services will really run in parallel because they are computed on other computers. Another good scenario is the microservices. We can delegate expensive computations to different Python microservices.
* Disadvantages: CPU-bound multi-threaded tasks have a performance bottleneck. These are expensive computations by nature, like matrix operations, numerical computations, and algorithms with high complexity. The most common workaround is to use Python libraries implemented in the C or C++ languages that are not limited by the GIL. A slightly more complex solution is to create one of these libraries. A modern solution is to use Python-compatible languages or Python supersets.