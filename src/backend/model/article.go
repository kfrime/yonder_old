package model

import (
	"time"
)

type Article struct {
	Id 			uint32
	AuthorId 	uint32
	CateId 		uint32
	Title 		string
	created 	time.Duration
	updated 	time.Duration
}

