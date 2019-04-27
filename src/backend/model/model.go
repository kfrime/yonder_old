package model

import "github.com/microcosm-cc/bluemonday"

// It protects sites from XSS attacks
func PreventXSS(input string) string {
	return bluemonday.UGCPolicy().Sanitize(input)
}