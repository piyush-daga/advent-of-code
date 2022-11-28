package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readFile(fpath string) string {
	bData, err := os.ReadFile(fpath)
	check(err)

	return string(bData)
}

func getInitialList(lfit *[]int, data string) {
	for _, v := range strings.Split(data, ",") {
		i, err := strconv.Atoi(v)
		check(err)

		(*lfit) = append((*lfit), i)
	}
}

func growthPerDay(lfit *[]int) {
	for i := range *lfit {
		(*lfit)[i]--
		if (*lfit)[i] < 0 {
			(*lfit)[i] = 6
			(*lfit) = append((*lfit), 8)
		}
	}
}

func modelLanternFishGrowthRate(fpath string, days int) {
	var lanternFishInternalTimers []int
	data := readFile(fpath)

	getInitialList(&lanternFishInternalTimers, data)

	fmt.Printf("Initial State: %v\n", lanternFishInternalTimers)

	for i := 1; i <= days; i++ {
		growthPerDay(&lanternFishInternalTimers)
		// fmt.Printf("After %d days: %v\n", i, lanternFishInternalTimers)
	}

	// fmt.Println(lanternFishInternalTimers)
	fmt.Println("Total no of lanternfish: ", len(lanternFishInternalTimers))
}

func sum(s []int) int {
	result := 0
	for _, v := range s {
		result += v
	}

	return result
}

func explosiveLanternFist(fpath string, days int) {
	var lanternFishInternalTimers []int
	var cyclic [10]int
	data := readFile(fpath)

	getInitialList(&lanternFishInternalTimers, data)

	// Initial setup
	for _, v := range lanternFishInternalTimers {
		cyclic[v]++
	}

	fmt.Println(cyclic)

	for d := 0; d < days; d++ {
		today := int(math.Mod(float64(d), 10))
		cyclic[int(math.Mod(float64(today+7), 10))] += cyclic[today]

		if d == 50 || d == 51 {
			fmt.Println(d, cyclic)
		}
	}

	fmt.Printf("No of lanternfish after %d days are: %d\n", days, sum(cyclic[:]))
}

func main() {
	// modelLanternFishGrowthRate("./input/input_small", 80)
	explosiveLanternFist("./input/input_small", 80)
	// modelLanternFishGrowthRate("./input/input", 256)
}
