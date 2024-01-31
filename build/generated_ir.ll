; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
.2:
  %".3" = alloca i32
  store i32 13, i32* %".3"
  %".5" = load i32, i32* %".3"
  %".6" = sub i32 %".5", 3
  %".7" = add i32 %".6", 8
  store i32 %".7", i32* %".3"
}
