package main

import (
	"encoding/json"
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

type Coordinate struct {
	X int
	Y int
}

type Line struct {
	Start Coordinate
	End   Coordinate
}

type LineSegments []Line

func readFile(fpath string) string {
	bData, err := os.ReadFile(fpath)
	check(err)

	return string(bData)
}

func castInt(s string) int {
	conv, err := strconv.Atoi(s)
	check(err)

	return conv
}

func prettyPrint(i interface{}) string {
	s, _ := json.MarshalIndent(i, "", "    ")

	return string(s)
}

func createLineSegments(input string) LineSegments {
	var lines LineSegments

	for _, l := range strings.Split(input, "\n") {
		line := Line{}
		points := strings.Split(l, " -> ")
		for i, p := range points {
			rawCoordinates := strings.Split(p, ",")
			co := Coordinate{X: castInt(rawCoordinates[0]), Y: castInt(rawCoordinates[1])}

			if i == 0 {
				line.Start = co
			} else {
				line.End = co
			}
		}
		lines = append(lines, line)
	}

	return lines
}

func abs(v int) int {
	if v < 0 {
		v = -v
	}

	return v
}

func extractCoordinatesForLine(l Line, includeDiags bool) []Coordinate {
	// This automatically eliminates straight line problems
	var coOrdinates []Coordinate
	var min, max int

	if l.Start.X == l.End.X {
		if (l.Start.Y - l.End.Y) > 0 {
			min = l.End.Y
			max = l.Start.Y
		} else {
			min = l.Start.Y
			max = l.End.Y
		}
		for i := min; i <= max; i++ {
			coOrdinates = append(coOrdinates, Coordinate{X: l.Start.X, Y: i})
		}

		return coOrdinates
	}

	if l.Start.Y == l.End.Y {
		if (l.Start.X - l.End.X) > 0 {
			min = l.End.X
			max = l.Start.X
		} else {
			min = l.Start.X
			max = l.End.X
		}
		for i := min; i <= max; i++ {
			coOrdinates = append(coOrdinates, Coordinate{X: i, Y: l.Start.Y})
		}
		return coOrdinates
	}

	isDiagonal := abs((l.Start.X - l.End.X) / (l.Start.Y - l.End.Y))
	if isDiagonal == 1 {
		var xdiff, ydiff int
		x, y := l.Start.X, l.Start.Y

		if (l.Start.X - l.End.X) > 0 {
			xdiff = -1
		} else {
			xdiff = 1
		}
		if (l.Start.Y - l.End.Y) > 0 {
			ydiff = -1
		} else {
			ydiff = 1
		}

		for (x != l.End.X) && (y != l.End.Y) {
			coOrdinates = append(coOrdinates, Coordinate{X: x, Y: y})
			x += xdiff
			y += ydiff
		}
		coOrdinates = append(coOrdinates, Coordinate{X: l.End.X, Y: l.End.Y})

	}

	return coOrdinates
}

func prettyPrintBoard(b [][]int) {
	for _, val := range b {
		fmt.Println(val)
	}
}

func createMatrix(ls *LineSegments) {
	// Well in poor taste, we can just take the overall matrx size as 1000
	matrixSize := 1000

	board := make([][]int, matrixSize)
	for i := 0; i < matrixSize; i++ {
		board[i] = make([]int, matrixSize)
	}

	for _, l := range *ls {
		coordinates := extractCoordinatesForLine(l, true)

		for _, co := range coordinates {
			board[co.X][co.Y]++
		}
	}

	// More than 2 lines intersecting
	result := 0
	for _, row := range board {
		for _, val := range row {
			if val >= 2 {
				result++
			}
		}
	}

	fmt.Println("No of points where 2 or more lines intersect are: ", result)

	// prettyPrintBoard(board)
}

func identifyMostDangerousAreas(fpath string) {
	input := readFile(fpath)
	ls := createLineSegments(input)

	createMatrix(&ls)
}

func main() {
	// identifyMostDangerousAreas("./input/input_small")
	identifyMostDangerousAreas("./input/input")
}
