; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
.2:
  %".3" = alloca i32 (i32)*
  store i32 (i32)* @"__function1__", i32 (i32)** %".3"
  ret i32 0
}

define i32 @"__function1__"(i32 %".1")
{
.3:
  ret i32 %".1"
}
