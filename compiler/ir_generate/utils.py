from llvmlite import ir, binding


target_data: binding.TargetData = None


def sizeof(type_: ir.Type, *, as_type: type[int] | ir.Type = int) -> int | ir.Constant:
    return as_type(type_.get_abi_size(target_data))
