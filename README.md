# Memory Allocator Benchmarks

This is a collection of memory allocator benchmarks. All benchmarks belongs to
its own creators mentioned in corresponding README files.

## How to Use

```
git clone git@github.com/xinhuang/memory-allocator-benchmarks.git
cd memory-allocator-benchmarks
mkdir build
cd build
cmake .. -DALLOCATOR=<Allocator Name> -DALLOCATOR_PATH=<Your Allocator Path>
make
python bin/run.py
```
