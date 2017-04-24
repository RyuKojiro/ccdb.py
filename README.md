## What does it do?
ccdb.py creates a [JSON Compilation Database file](https://clang.llvm.org/docs/JSONCompilationDatabase.html) (`compile_commands.json`).

These are particularly useful for tools like [YouCompleteMe](https://github.com/Valloric/YouCompleteMe), which can use this output as an automatically generated indicator of how the code in a project is compiled, independent of the actual build system.

## How do I use it?
`ccdb.py` just man-in-the-middles your compiler. So, the answer basically boils down to changing `CC` to point to `ccdb.py` and setting `ACTUAL_CC` to what `CC` was.

Because build flags don't change very often, this is only intended to be done once, when you need to generate a `compile_commands.json`. Although, as long as you don't have a multi-compiler project, there is nothing really stopping you from setting up your build to run it every time; just remember to add a step that removes your `compile_commands.json` before each build.

### Make
For make, you can just build once adding the necessary variables, like so:

```
make CC=/the/path/to/ccdb/ccdb.py ACTUAL_CC=clang
```

### Xcode
I'm working on an plugin to add `ccdb.py` support to Xcode, but it's not done, yet.

### CMake
This tool isn't necessary for CMake, just set `CMAKE_EXPORT_COMPILE_COMMANDS` to `ON`.

### Ninja
Ninja has the `compdb` tool, which solves this.

## But what about [insert language here]?
Languages like Objective-C are quite simple, since you generally use the same compiler for C and Objective-C. C++ also works the same way, but only in pure C++ projects. However, mixed language projects that involve invoking two different compilers (like C/C++ together), require you to run it once for each compiler or assembler that is mixed in.