package main

import (
	"fmt"
	"os"
)

//go:generate go run "github.com/Jumpaku/cyamli/cmd/cyamli@latest" golang -schema-path=cli.yaml -out-path=cli.gen.go
func main() {
	// Create the CLI object
	cli := NewCLI()
	// Overwrite behaviors
	cli.FUNC = showHelp
	cli.Hello.FUNC = sayHello
	// Run with command line arguments
	if err := Run(cli, os.Args); err != nil {
		panic(err)
	}
}

func showHelp(subcommand []string, input CLI_Input, inputErr error) (err error) {
	if input.Opt_Help {
		fmt.Println("This is an example program.")
	} else {
		fmt.Println("Do nothing.")
	}
	return nil
}
func sayHello(subcommand []string, input CLI_Hello_Input, inputErr error) (err error) {
	hello := "Hello"
	if input.Opt_TargetName != "" {
		hello += ", " + input.Opt_TargetName
	}
	hello += "! My name is " + input.Arg_Greeter + "!"
	fmt.Println(hello)
	return nil
}
