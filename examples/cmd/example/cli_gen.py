# Code generated by github.com/Jumpaku/cyamli v1.1.0, DO NOT EDIT.

from dataclasses import dataclass
import typing


@dataclass
class CLI_Sub3Subd_Input:
    
    arg_arg_v: tuple[str,...] = tuple[str,...]()
    
    pass


class CLI_Sub3Subd:
    
    FUNC: typing.Callable[[None,list[str],CLI_Sub3Subd_Input,Exception],None] = None


def resolve_CLI_Sub3Subd_Input(rest_args: list[str])->CLI_Sub3Subd_Input:
    input = CLI_Sub3Subd_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        
        raise Exception("unsupported option " + opt_name)
    if len(arguments) <= 0 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[str,...], *arguments[0:])
    
    return input


@dataclass
class CLI_Sub3Subc_Input:
    
    arg_arg_v: tuple[float,...] = tuple[float,...]()
    
    pass


class CLI_Sub3Subc:
    
    FUNC: typing.Callable[[None,list[str],CLI_Sub3Subc_Input,Exception],None] = None


def resolve_CLI_Sub3Subc_Input(rest_args: list[str])->CLI_Sub3Subc_Input:
    input = CLI_Sub3Subc_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        
        raise Exception("unsupported option " + opt_name)
    if len(arguments) <= 0 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[float,...], *arguments[0:])
    
    return input


@dataclass
class CLI_Sub3Subb_Input:
    
    arg_arg_v: tuple[int,...] = tuple[int,...]()
    
    pass


class CLI_Sub3Subb:
    
    FUNC: typing.Callable[[None,list[str],CLI_Sub3Subb_Input,Exception],None] = None


def resolve_CLI_Sub3Subb_Input(rest_args: list[str])->CLI_Sub3Subb_Input:
    input = CLI_Sub3Subb_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        
        raise Exception("unsupported option " + opt_name)
    if len(arguments) <= 0 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[int,...], *arguments[0:])
    
    return input


@dataclass
class CLI_Sub3Suba_Input:
    
    arg_arg_v: tuple[bool,...] = tuple[bool,...]()
    
    pass


class CLI_Sub3Suba:
    
    FUNC: typing.Callable[[None,list[str],CLI_Sub3Suba_Input,Exception],None] = None


def resolve_CLI_Sub3Suba_Input(rest_args: list[str])->CLI_Sub3Suba_Input:
    input = CLI_Sub3Suba_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        
        raise Exception("unsupported option " + opt_name)
    if len(arguments) <= 0 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[bool,...], *arguments[0:])
    
    return input


@dataclass
class CLI_Sub3_Input:
    opt_option_a: str = "abc"
    opt_option_b: int = int(-123)
    opt_option_c: bool = True
    opt_option_d: float = float(-123.456)
    opt_option_e: str = ""
    
    arg_arg_a: str = str()
    arg_arg_b: int = int()
    arg_arg_c: bool = bool()
    arg_arg_d: float = float()
    arg_arg_e: str = str()
    arg_arg_v: tuple[str,...] = tuple[str,...]()
    
    pass


class CLI_Sub3:
    subd: CLI_Sub3Subd = CLI_Sub3Subd()
    subc: CLI_Sub3Subc = CLI_Sub3Subc()
    subb: CLI_Sub3Subb = CLI_Sub3Subb()
    suba: CLI_Sub3Suba = CLI_Sub3Suba()
    
    FUNC: typing.Callable[[None,list[str],CLI_Sub3_Input,Exception],None] = None


def resolve_CLI_Sub3_Input(rest_args: list[str])->CLI_Sub3_Input:
    input = CLI_Sub3_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        
        if opt_name == "-option-a" or opt_name == "-a":
            if not assign:
                raise Exception("value is not specified to option "+ opt_name)
                
            input.opt_option_a = parse_value(str, split[1])
            continue
        
        if opt_name == "-option-b" or opt_name == "-b":
            if not assign:
                raise Exception("value is not specified to option "+ opt_name)
                
            input.opt_option_b = parse_value(int, split[1])
            continue
        
        if opt_name == "-option-c" or opt_name == "-c":
            if not assign:
                split.append("True")
                
            input.opt_option_c = parse_value(bool, split[1])
            continue
        
        if opt_name == "-option-d" or opt_name == "-d":
            if not assign:
                raise Exception("value is not specified to option "+ opt_name)
                
            input.opt_option_d = parse_value(float, split[1])
            continue
        
        if opt_name == "-option-e":
            if not assign:
                raise Exception("value is not specified to option "+ opt_name)
                
            input.opt_option_e = parse_value(str, split[1])
            continue
        
        raise Exception("unsupported option " + opt_name)
    if len(arguments) <= 0:
        raise Exception("too few arguments")
    input.arg_arg_a = parse_value(str, arguments[0])
    if len(arguments) <= 1:
        raise Exception("too few arguments")
    input.arg_arg_b = parse_value(int, arguments[1])
    if len(arguments) <= 2:
        raise Exception("too few arguments")
    input.arg_arg_c = parse_value(bool, arguments[2])
    if len(arguments) <= 3:
        raise Exception("too few arguments")
    input.arg_arg_d = parse_value(float, arguments[3])
    if len(arguments) <= 4:
        raise Exception("too few arguments")
    input.arg_arg_e = parse_value(str, arguments[4])
    if len(arguments) <= 5 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[str,...], *arguments[5:])
    
    return input


@dataclass
class CLI_Sub2_Input:
    
    
    pass


class CLI_Sub2:
    
    FUNC: typing.Callable[[None,list[str],CLI_Sub2_Input,Exception],None] = None


def resolve_CLI_Sub2_Input(rest_args: list[str])->CLI_Sub2_Input:
    input = CLI_Sub2_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        
        raise Exception("unsupported option " + opt_name)
    
    return input


@dataclass
class CLI_Sub1_Input:
    
    
    pass


class CLI_Sub1:
    
    FUNC: typing.Callable[[None,list[str],CLI_Sub1_Input,Exception],None] = None


def resolve_CLI_Sub1_Input(rest_args: list[str])->CLI_Sub1_Input:
    input = CLI_Sub1_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        
        raise Exception("unsupported option " + opt_name)
    
    return input


@dataclass
class CLI_Input:
    opt_option_a: str = "abc"
    opt_option_b: int = int(-123)
    opt_option_c: bool = True
    opt_option_d: float = float(-123.456)
    opt_option_e: str = ""
    
    arg_arg_a: str = str()
    arg_arg_b: int = int()
    arg_arg_c: bool = bool()
    arg_arg_d: float = float()
    arg_arg_e: str = str()
    arg_arg_v: tuple[str,...] = tuple[str,...]()
    
    pass


class CLI:
    sub3: CLI_Sub3 = CLI_Sub3()
    sub2: CLI_Sub2 = CLI_Sub2()
    sub1: CLI_Sub1 = CLI_Sub1()
    
    FUNC: typing.Callable[[None,list[str],CLI_Input,Exception],None] = None


def resolve_CLI_Input(rest_args: list[str])->CLI_Input:
    input = CLI_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        
        if opt_name == "-option-a" or opt_name == "-a":
            if not assign:
                raise Exception("value is not specified to option "+ opt_name)
                
            input.opt_option_a = parse_value(str, split[1])
            continue
        
        if opt_name == "-option-b" or opt_name == "-b":
            if not assign:
                raise Exception("value is not specified to option "+ opt_name)
                
            input.opt_option_b = parse_value(int, split[1])
            continue
        
        if opt_name == "-option-c" or opt_name == "-c":
            if not assign:
                split.append("True")
                
            input.opt_option_c = parse_value(bool, split[1])
            continue
        
        if opt_name == "-option-d" or opt_name == "-d":
            if not assign:
                raise Exception("value is not specified to option "+ opt_name)
                
            input.opt_option_d = parse_value(float, split[1])
            continue
        
        if opt_name == "-option-e":
            if not assign:
                raise Exception("value is not specified to option "+ opt_name)
                
            input.opt_option_e = parse_value(str, split[1])
            continue
        
        raise Exception("unsupported option " + opt_name)
    if len(arguments) <= 0:
        raise Exception("too few arguments")
    input.arg_arg_a = parse_value(str, arguments[0])
    if len(arguments) <= 1:
        raise Exception("too few arguments")
    input.arg_arg_b = parse_value(int, arguments[1])
    if len(arguments) <= 2:
        raise Exception("too few arguments")
    input.arg_arg_c = parse_value(bool, arguments[2])
    if len(arguments) <= 3:
        raise Exception("too few arguments")
    input.arg_arg_d = parse_value(float, arguments[3])
    if len(arguments) <= 4:
        raise Exception("too few arguments")
    input.arg_arg_e = parse_value(str, arguments[4])
    if len(arguments) <= 5 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[str,...], *arguments[5:])
    
    return input


def run(cli: CLI, args: list[str]):
    r = resolve_subcommand(args)
    subcommand_path, rest_args = r.subcommand, r.rest_args
    joined_subcommand = " ".join(subcommand_path)
    
    if joined_subcommand == "":
        if not cli.FUNC:
            raise Exception("unsupported subcommand \"" + "" + "\": cli.FUNC not assigned")
        ex: Exception = None
        input: CLI_Input = None
        try:
            input = resolve_CLI_Input(rest_args)
        except Exception as e:
            ex = e
        cli.FUNC(subcommand_path, input, ex)
    
    
    if joined_subcommand == "sub3 subd":
        if not cli.sub3.subd.FUNC:
            raise Exception("unsupported subcommand \"" + "sub3 subd" + "\": cli.sub3.subd.FUNC not assigned")
        ex: Exception = None
        input: CLI_Sub3Subd_Input = None
        try:
            input = resolve_CLI_Sub3Subd_Input(rest_args)
        except Exception as e:
            ex = e
        cli.sub3.subd.FUNC(subcommand_path, input, ex)
    
    if joined_subcommand == "sub3 subc":
        if not cli.sub3.subc.FUNC:
            raise Exception("unsupported subcommand \"" + "sub3 subc" + "\": cli.sub3.subc.FUNC not assigned")
        ex: Exception = None
        input: CLI_Sub3Subc_Input = None
        try:
            input = resolve_CLI_Sub3Subc_Input(rest_args)
        except Exception as e:
            ex = e
        cli.sub3.subc.FUNC(subcommand_path, input, ex)
    
    if joined_subcommand == "sub3 subb":
        if not cli.sub3.subb.FUNC:
            raise Exception("unsupported subcommand \"" + "sub3 subb" + "\": cli.sub3.subb.FUNC not assigned")
        ex: Exception = None
        input: CLI_Sub3Subb_Input = None
        try:
            input = resolve_CLI_Sub3Subb_Input(rest_args)
        except Exception as e:
            ex = e
        cli.sub3.subb.FUNC(subcommand_path, input, ex)
    
    if joined_subcommand == "sub3 suba":
        if not cli.sub3.suba.FUNC:
            raise Exception("unsupported subcommand \"" + "sub3 suba" + "\": cli.sub3.suba.FUNC not assigned")
        ex: Exception = None
        input: CLI_Sub3Suba_Input = None
        try:
            input = resolve_CLI_Sub3Suba_Input(rest_args)
        except Exception as e:
            ex = e
        cli.sub3.suba.FUNC(subcommand_path, input, ex)
    
    if joined_subcommand == "sub3":
        if not cli.sub3.FUNC:
            raise Exception("unsupported subcommand \"" + "sub3" + "\": cli.sub3.FUNC not assigned")
        ex: Exception = None
        input: CLI_Sub3_Input = None
        try:
            input = resolve_CLI_Sub3_Input(rest_args)
        except Exception as e:
            ex = e
        cli.sub3.FUNC(subcommand_path, input, ex)
    
    if joined_subcommand == "sub2":
        if not cli.sub2.FUNC:
            raise Exception("unsupported subcommand \"" + "sub2" + "\": cli.sub2.FUNC not assigned")
        ex: Exception = None
        input: CLI_Sub2_Input = None
        try:
            input = resolve_CLI_Sub2_Input(rest_args)
        except Exception as e:
            ex = e
        cli.sub2.FUNC(subcommand_path, input, ex)
    
    if joined_subcommand == "sub1":
        if not cli.sub1.FUNC:
            raise Exception("unsupported subcommand \"" + "sub1" + "\": cli.sub1.FUNC not assigned")
        ex: Exception = None
        input: CLI_Sub1_Input = None
        try:
            input = resolve_CLI_Sub1_Input(rest_args)
        except Exception as e:
            ex = e
        cli.sub1.FUNC(subcommand_path, input, ex)
    
    raise Exception("subcommand not found: " + joined_subcommand)

@dataclass
class ResolveSubcommandResult:
    subcommand: list[str]
    rest_args: list[str]


def resolve_subcommand(args: list[str])->ResolveSubcommandResult:
    if not args:
        raise Exception("command line arguments are too few")
    
    subcommand_set = {
        "",
        "sub3 subd","sub3 subc","sub3 subb","sub3 suba","sub3","sub2","sub1",
    }

    subcommand_path = []
    for arg in args[1:]:
        if arg == "--":
            break
        if " ".join(subcommand_path + [arg]) not in subcommand_set:
            break
        subcommand_path.append(arg)
    
    return ResolveSubcommandResult(subcommand_path, args[1+len(subcommand_path):])


def parse_value(typ, *str_values: str) -> typing.Union[str, bool, float, int, tuple[str, ...], tuple[bool, ...], tuple[float, ...], tuple[int, ...]]:
    try: 
        if typ == str:
            return str(str_values[0])
        if typ == bool:
            if str_values[0] in {"", "0", "f", "F", "FALSE", "false", "False"}:
                return False
            if str_values[0] in {"1", "t", "T", "TRUE", "true", "True"}:
                return True
            raise Exception("could not convert string to bool: '" + str_values[0] + "'")
        if typ == float:
            return float(str_values[0])
        if typ == int:
            return int(str_values[0], base=0)
        if typ == tuple[str,...]:
            return tuple([parse_value(str, s) for s in str_values])
        if typ == tuple[bool,...]:
            return tuple([parse_value(bool, s) for s in str_values])
        if typ == tuple[float,...]:
            return tuple([parse_value(float, s) for s in str_values])
        if typ == tuple[int,...]:
            return tuple([parse_value(int, s) for s in str_values])
        raise Exception("unsupported type")
    except Exception as e:
        e.add_note('fail to parse string value as ' + typ.__name__)
        raise


def get_doc(subcommand: list[str]) -> str:
    joined_subcommand = " ".join(subcommand)
    
    if joined_subcommand == "":
        return "example (v1.0.0)\n\nexample\n\n    Description:\n        this is an example command\n\n    Syntax:\n        $ example  [<option>|<argument>]... [-- [<argument>]...]\n\n    Options:\n        -option-a=<string>, -a=<string>  (default=\"abc\"):\n            a - this is an option for root command\n\n        -option-b=<integer>, -b=<integer>  (default=-123):\n            b - this is an option for root command\n\n        -option-c[=<boolean>], -c[=<boolean>]  (default=true):\n            c - this is an option for root command\n\n        -option-d=<float>, -d=<float>  (default=-123.456):\n            d - this is an option for root command\n\n        -option-e=<string>  (default=\"\"):\n\n    Arguments:\n        1.  <arg_a:string>\n            a - this is an argument for root command\n\n        2.  <arg_b:integer>\n            b - this is an argument for root command\n\n        3.  <arg_c:boolean>\n            c - this is an argument for root command\n\n        4.  <arg_d:float>\n            d - this is an argument for root command\n\n        5.  <arg_e:string>\n\n        6. [<arg_v:string>]...\n            v - this is an argument for root command\n\n    Subcommands:\n        sub1:\n            1 - this is a sub command\n\n        sub2:\n            2 - this is a sub command\n\n        sub3:\n            3 - this is a sub command\n\n\n"
    
    
    if joined_subcommand == "sub3 subd":
        return "example (v1.0.0)\n\nexample sub3 subd\n\n    Syntax:\n        $ example sub3 subd [<argument>]... [-- [<argument>]...]\n\n    Arguments:\n        1. [<arg_v:string>]...\n\n\n"
    
    if joined_subcommand == "sub3 subc":
        return "example (v1.0.0)\n\nexample sub3 subc\n\n    Syntax:\n        $ example sub3 subc [<argument>]... [-- [<argument>]...]\n\n    Arguments:\n        1. [<arg_v:float>]...\n\n\n"
    
    if joined_subcommand == "sub3 subb":
        return "example (v1.0.0)\n\nexample sub3 subb\n\n    Syntax:\n        $ example sub3 subb [<argument>]... [-- [<argument>]...]\n\n    Arguments:\n        1. [<arg_v:integer>]...\n\n\n"
    
    if joined_subcommand == "sub3 suba":
        return "example (v1.0.0)\n\nexample sub3 suba\n\n    Syntax:\n        $ example sub3 suba [<argument>]... [-- [<argument>]...]\n\n    Arguments:\n        1. [<arg_v:boolean>]...\n\n\n"
    
    if joined_subcommand == "sub3":
        return "example (v1.0.0)\n\nexample sub3\n\n    Description:\n        3 - this is a sub command\n\n    Syntax:\n        $ example sub3 [<option>|<argument>]... [-- [<argument>]...]\n\n    Options:\n        -option-a=<string>, -a=<string>  (default=\"abc\"):\n            3 - a - this is an option for root command\n\n        -option-b=<integer>, -b=<integer>  (default=-123):\n            3 - b - this is an option for root command\n\n        -option-c[=<boolean>], -c[=<boolean>]  (default=true):\n            3 - c - this is an option for root command\n\n        -option-d=<float>, -d=<float>  (default=-123.456):\n            3 - d - this is an option for root command\n\n        -option-e=<string>  (default=\"\"):\n\n    Arguments:\n        1.  <arg_a:string>\n            3 - a - this is an argument for root command\n\n        2.  <arg_b:integer>\n            3 - b - this is an argument for root command\n\n        3.  <arg_c:boolean>\n            3 - c - this is an argument for root command\n\n        4.  <arg_d:float>\n            3 - d - this is an argument for root command\n\n        5.  <arg_e:string>\n\n        6. [<arg_v:string>]...\n            3 - v - this is an argument for root command\n\n    Subcommands:\n        suba:\n\n        subb:\n\n        subc:\n\n        subd:\n\n\n"
    
    if joined_subcommand == "sub2":
        return "example (v1.0.0)\n\nexample sub2\n\n    Description:\n        2 - this is a sub command\n\n    Syntax:\n        $ example sub2\n\n\n"
    
    if joined_subcommand == "sub1":
        return "example (v1.0.0)\n\nexample sub1\n\n    Description:\n        1 - this is a sub command\n\n    Syntax:\n        $ example sub1\n\n\n"
    
    raise Exception("subcommand not found: " + joined_subcommand)
