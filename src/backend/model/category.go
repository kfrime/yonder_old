package model

import (
	"time"
)

type Category struct {
	Id 			uint32
	Name 		string
	created 	time.Duration
	updated 	time.Duration
}
