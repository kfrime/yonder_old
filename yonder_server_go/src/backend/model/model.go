package model

import (
	"github.com/microcosm-cc/bluemonday"
	"time"
)

type BaseModel struct {
	ID 			uint `gorm:"primary_key"`
	CreatedAt   time.Time
	UpdatedAt   time.Time
}

// It protects sites from XSS attacks
func PreventXSS(input string) string {
	return bluemonday.UGCPolicy().Sanitize(input)
}