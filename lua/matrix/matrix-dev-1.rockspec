package = "matrix"
version = "dev-1"
source = {
   url = "git+ssh://git@github.com/cam5/exercism.git"
}
description = {
   summary = "Welcome to Matrix on Exercism's Lua Track.",
   detailed = [[
Welcome to Matrix on Exercism's Lua Track.
If you need help running the tests or submitting your code, check out `HELP.md`.]],
   homepage = "*** please enter a project homepage ***",
   license = "*** please specify a license ***"
}
dependencies = {
   "json-lua >= 0.1",
}
build = {
   type = "builtin",
   modules = {
      matrix = "matrix.lua",
      matrix_spec = "matrix_spec.lua"
   }
}
