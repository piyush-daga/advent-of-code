package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readInput(fpath string) []string {
	bData, err := os.ReadFile(fpath)
	check(err)

	return strings.Split(string(bData), "\n")
}

// func

func part1(inputArr []string) {
	horizontalPos, verticalPos := 0, 0

	for _, val := range inputArr {
		movIdentifiers := strings.Split(val, " ")
		movVal, err := strconv.Atoi(movIdentifiers[1])
		check(err)
		movType := movIdentifiers[0]

		switch movType {
		case "forward":
			horizontalPos += movVal
		case "down":
			verticalPos += movVal
		case "up":
			verticalPos -= movVal
		}
	}

	fmt.Println(horizontalPos, verticalPos)
	fmt.Println(horizontalPos * verticalPos)

}

func part2(inputArr []string) {
	horizontalPos, verticalPos, aim := 0, 0, 0

	for _, val := range inputArr {
		movIdentifiers := strings.Split(val, " ")
		movVal, err := strconv.Atoi(movIdentifiers[1])
		check(err)
		movType := movIdentifiers[0]

		switch movType {
		case "forward":
			horizontalPos += movVal
			verticalPos += movVal * aim
		case "down":
			aim += movVal
		case "up":
			aim -= movVal
		}
	}

	fmt.Println(horizontalPos, verticalPos)
	fmt.Println(horizontalPos * verticalPos)
}

func main() {
	inputArr := readInput("./input/input")
	// part1(inputArr)
	part2(inputArr)
}
