// Code generated by cliautor 0.0.0, DO NOT EDIT.
package main

import (
	"fmt"
	"bytes"
	"strings"
	"os"

	cliautor_schema "github.com/Jumpaku/cliautor/schema"
	cliautor_golang "github.com/Jumpaku/cliautor/golang"
	cliautor_description "github.com/Jumpaku/cliautor/description"
)

func newSchema() *cliautor_schema.Schema {
	var schema, _ = cliautor_schema.Load(bytes.NewBufferString("name: cliautor\nversion: v1.0.0\ndescription: A command line tool to generate CLI for your app from YAML-based schema.\noptions:\n  -help:\n    short: -h\n    description: shows description of this app\n    type: boolean\n    default: \"\"\n  -version:\n    short: -v\n    description: shows version of this app\n    type: boolean\n    default: \"\"\narguments: []\nsubcommands:\n  golang:\n    description: generates CLI for your app written in Go.\n    options:\n      -help:\n        short: -h\n        description: shows description of golang subcommand\n        type: boolean\n        default: \"\"\n      -out-path:\n        short: \"\"\n        description: if specified then creates a file at the path and writes generated code, otherwise outputs to stdout.\n        type: \"\"\n        default: \"\"\n      -package:\n        short: \"\"\n        description: package name where the generated file will be placed.\n        type: \"\"\n        default: main\n      -schema-path:\n        short: \"\"\n        description: if specified then reads schema file from the path, otherwise reads from stdin.\n        type: \"\"\n        default: \"\"\n    arguments: []\n    subcommands: {}\n"))
	return schema
}


type Func[Input any] func(cmdSchema *cliautor_schema.Command, subcommand []string, input Input) (err error)




type CLI struct {
	Sub_Golang CLI_Golang

	Func Func[CLI_Input]
}

type CLI_Input struct {
	Opt_Help bool
	Opt_Version bool


}







type CLI_Golang struct {

	Func Func[CLI_Golang_Input]
}

type CLI_Golang_Input struct {
	Opt_Help bool
	Opt_OutPath string
	Opt_Package string
	Opt_SchemaPath string


}




func NewCLI() CLI {
	cli := CLI{}
	s := newSchema()

	cli.Func = cliautor_golang.NewDefaultFunc[CLI_Input](s.Program.Name)


	cli.Sub_Golang.Func = cliautor_golang.NewDefaultFunc[CLI_Golang_Input](s.Program.Name)

	return cli
}


func Run(cli CLI, args []string) error {
	s := newSchema()
	cmd, subcommand, restArgs := cliautor_golang.ResolveSubcommand(s, args)
	switch strings.Join(subcommand, " ") {

	case "":
		input := CLI_Input{
			Opt_Help: false,
			Opt_Version: false,

		}
		if err := cliautor_golang.ResolveInput(cmd, restArgs, &input); err != nil {
			descData := cliautor_description.CreateCommandData(s.Program.Name, subcommand, cmd)
			if err := cliautor_description.DescribeCommand(cliautor_description.SimpleExecutor(), descData, os.Stderr); err != nil {
				panic(fmt.Errorf("fail to create command description: %w", err))
			}
			return fmt.Errorf("fail to resolve input: %w", err)
		}
		funcMethod := cli.Func
		if funcMethod == nil {
			return fmt.Errorf("%q is unsupported: cli.Func not assigned", "")
		}
		if err := funcMethod(cmd, subcommand, input); err != nil {
			return fmt.Errorf("cli.Func(input) failed: %w", err)
		}


	case "golang":
		input := CLI_Golang_Input{
			Opt_Help: false,
			Opt_OutPath: "",
			Opt_Package: "main",
			Opt_SchemaPath: "",

		}
		if err := cliautor_golang.ResolveInput(cmd, restArgs, &input); err != nil {
			descData := cliautor_description.CreateCommandData(s.Program.Name, subcommand, cmd)
			if err := cliautor_description.DescribeCommand(cliautor_description.SimpleExecutor(), descData, os.Stderr); err != nil {
				panic(fmt.Errorf("fail to create command description: %w", err))
			}
			return fmt.Errorf("fail to resolve input: %w", err)
		}
		funcMethod := cli.Sub_Golang.Func
		if funcMethod == nil {
			return fmt.Errorf("%q is unsupported: cli.Sub_Golang.Func not assigned", "golang")
		}
		if err := funcMethod(cmd, subcommand, input); err != nil {
			return fmt.Errorf("cli.Sub_Golang.Func(input) failed: %w", err)
		}

	}
	return nil
}
