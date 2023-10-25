extern "C" int parser_main(int argc, const char* argv[]);

int main(int argc, const char* argv[])
{
	const char* forward_argv[] = {argv[0], "input.shf"};
	int forward_argc = argc + 1;

	return parser_main(forward_argc, forward_argv);
}