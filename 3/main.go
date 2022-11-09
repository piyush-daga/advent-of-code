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

// func parseData(input []string) []

func bitsToInt(data string) int64 {
	converted, err := strconv.ParseInt(data, 2, 64)
	check(err)

	return converted

}

func part1better(ip []string) {
	individualIpLength := len(ip[0])
	totalIps := len(ip)

	zeroes := make([]int, individualIpLength)

	for _, bits := range ip {
		for i := 0; i < individualIpLength; i++ {
			// Ascii for 0 -> 48
			if bits[i] == 48 {
				zeroes[i]++
			}
		}
	}

	gammaBits, epsilionBits := "", ""
	for _, val := range zeroes {
		if val > totalIps/2 {
			gammaBits += "0"
			epsilionBits += "1"
		} else {
			gammaBits += "1"
			epsilionBits += "0"
		}
	}
	gammaRate := bitsToInt(gammaBits)
	epsilionRate := bitsToInt(epsilionBits)

	fmt.Println("Gamma Rate: ", gammaRate)
	fmt.Println("Epsilion Rate: ", epsilionRate)
	fmt.Println("Power Consumption", gammaRate*epsilionRate)
}

func part1(ip []string) {
	// Considering all bits to have same length
	individualIpLength := len(ip[0])
	result := make([]map[string]int, individualIpLength)
	gammaBits, epsilionBits := "", ""

	for _, bits := range ip {

		for i := 0; i < individualIpLength; i++ {
			if result[i] == nil {
				result[i] = make(map[string]int)
			}
			result[i][string(bits[i])]++
		}
	}

	// Reconcile for gamma and epsilion rate
	// We could easily bit flip for epsilion rate instead of accounting for it.
	for _, bits := range result {
		higher, lower := "", ""
		switch bits["0"] > bits["1"] {
		case true:
			higher = "0"
			lower = "1"
		case false:
			higher = "1"
			lower = "0"
		}
		gammaBits += higher
		epsilionBits += lower
	}

	// fmt.Println(gammaBits, epsilionBits)
	gammaRate := bitsToInt(gammaBits)
	epsilionRate := bitsToInt(epsilionBits)

	fmt.Println("Gamma Rate: ", gammaRate)
	fmt.Println("Epsilion Rate: ", epsilionRate)
	fmt.Println("Power Consumption", gammaRate*epsilionRate)
}

func part2() {

}

func main() {
	ip := readInput("./3/input/input")
	// part1(ip)
	part1better(ip)
}
