package data

import (
	"cliautor/name"
)

type Subcommand struct {
	Name name.Path
}

func (d Subcommand) SubcommandFieldName() string {
	return "Sub_" + name.Title(d.Name[len(d.Name)-1])
}

func (d Subcommand) SubcommandFieldType() string {
	return d.Name.Map(name.Title).Join("", "CLI_", "")
}
