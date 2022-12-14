package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Board [5][5]string

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func inputCorrection(row string) string {
	row = strings.Replace(row, "  ", " ", -1)
	row = strings.TrimSpace(row)

	return row
}

func createBingoBoard(ip string) Board {
	board := Board{}

	for i, val := range strings.Split(ip, "\n") {
		val = inputCorrection(val)
		for j, item := range strings.Split(val, " ") {
			board[i][j] = item
		}
	}

	return board
}

func readInput(fpath string) ([]string, []Board) {
	var numDraw []string

	bData, err := os.ReadFile(fpath)
	check(err)

	data := string(bData)

	splits := strings.Split(data, "\n\n")

	numDraw = strings.Split(splits[0], ",")

	boards := make([]Board, len(splits[1:]))
	for i, val := range splits[1:] {
		boards[i] = createBingoBoard(val)
	}

	return numDraw, boards
}

func (b *Board) isComplete() bool {
	complete := false
	count := 0

	// Only check row completeness here
	for _, row := range *b {
		count = 0
		for _, col := range row {
			if col != "x" {
				continue
			}
			count++
		}
		// If row is complete
		if count == 5 {
			complete = true
			break
		}
	}

	if complete {
		return complete
	}

	// Check column completeness
	for i := range *b {
		count = 0
		for j := range (*b)[i] {
			if (*b)[j][i] != "x" {
				continue
			}
			count++
		}
		if count == 5 {
			complete = true
			break
		}
	}

	return complete
}

func (b *Board) sum() int {
	sum := 0

	for _, row := range *b {
		for _, col := range row {
			if col == "x" {
				continue
			}
			val, err := strconv.Atoi(col)
			check(err)
			sum += val
		}
	}

	return sum
}

func (b *Board) prettyPrint() {
	for _, row := range *b {
		for _, col := range row {
			fmt.Printf("%s ", col)
		}
		fmt.Println()
	}
	fmt.Printf("\n\n")
}

func (b *Board) mark(draw string) {
	// Marking entries is equivalent of making them nil? Or ''
	for j, row := range *b {
		for k, col := range row {
			if col == draw {
				(*b)[j][k] = "x"
				break
			}
		}
	}
}

func runBingoSimulationPart1(draws []string, boards []Board) {

	var completedBoardIndex int
	var latestDraw int
	complete := false

	for _, d := range draws {
		for i := range boards {
			boards[i].mark(d)
			fmt.Println("Draw is: ", d)
			boards[i].prettyPrint()
			if boards[i].isComplete() {
				completedBoardIndex = i
				latestDraw, _ = strconv.Atoi(d)
				complete = true

				break
			}
		}
		if complete {
			break
		}
	}

	fmt.Println("Completed board index", completedBoardIndex)
	fmt.Println("Sum of elements of winning board", boards[completedBoardIndex].sum())
	fmt.Println("Final Score", boards[completedBoardIndex].sum()*latestDraw)
}

func inSlice(vals []int, k int) bool {
	for _, v := range vals {
		if v == k {
			return true
		}
	}

	return false
}

func runBingoSimulationPart2(draws []string, boards []Board) {
	// We have to traverse till the last winning board
	var completedBoardIndex int
	var latestDraw int
	complete := false

	// It should not hold all the boards
	completedBoardIndexes := make([]int, 0, len(boards))

	for _, d := range draws {
		// fmt.Println("Draw is: ", d)

		for i := range boards {
			if inSlice(completedBoardIndexes, i) {
				continue
			}
			boards[i].mark(d)

			fmt.Println("Draw is: ", d)
			boards[i].prettyPrint()

			if boards[i].isComplete() {
				completedBoardIndexes = append(completedBoardIndexes, i)

				if len(completedBoardIndexes) == len(boards) {
					completedBoardIndex = i
					latestDraw, _ = strconv.Atoi(d)
					complete = true

					break
				}
			}
		}
		if complete {
			break
		}
	}

	fmt.Println("Completed board index", completedBoardIndex)
	fmt.Println("Sum of elements of winning board", boards[completedBoardIndex].sum())
	fmt.Println("Final Score", boards[completedBoardIndex].sum()*latestDraw)
}

func main() {
	draws, boards := readInput("./input/input")
	runBingoSimulationPart1(draws, boards)
	runBingoSimulationPart2(draws, boards)
}
