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

func readInput(fpath string) []int {
	var depths []int
	bData, err := os.ReadFile(fpath)
	check(err)

	for _, str := range strings.Split(string(bData), "\n") {
		depth, err := strconv.Atoi(str)
		check(err)

		depths = append(depths, depth)
	}

	return depths
}

func increasingDepth(depths *[]int) {
	increased := 0

	for i := range *depths {
		if i == 0 {
			continue
		}
		if (*depths)[i] > (*depths)[i-1] {
			increased++
		}
	}

	fmt.Println("No of times depth increased is: ", increased)
}

func sum(vals []int) int {
	result := 0
	for _, v := range vals {
		result += v
	}

	return result
}

func slidingWindowIncreasingDepth(depths *[]int) {
	increased := 0
	windowSize := 3
	previousMeasurment := 0
	currentMeasurment := 0

	for i := range (*depths)[:len(*depths)-2] {
		if i == 0 {
			previousMeasurment = sum((*depths)[i : i+windowSize])
			continue
		}
		currentMeasurment = sum((*depths)[i : i+windowSize])
		if currentMeasurment > previousMeasurment {
			increased++
		}
		previousMeasurment = currentMeasurment
	}

	fmt.Println("No of times depth increased in a sliding window calc is: ", increased)
}

func main() {
	depths := readInput("./input/input")
	increasingDepth(&depths)
	slidingWindowIncreasingDepth(&depths)
}
