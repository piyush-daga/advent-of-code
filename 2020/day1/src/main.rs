// Two entries multiplying to 2020
// Soln: Add all values to a hashmap, and then iterate over the original arr and find if the diff val exists as
// a key

use anyhow::{Ok, Result};
use itertools::Itertools;

fn main() -> anyhow::Result<()> {
    // This expects the file to be present at runtime, which is dangerous, instead we can include it at compile time
    // let s = std::fs::read_to_string("./src/input_small.txt")?;
    let (x, y) = include_str!("input.txt")
        .lines()
        .map(str::parse::<i64>)
        .collect::<Result<Vec<_>, _>>()?
        .into_iter()
        .tuple_combinations()
        .find(|(x, y)| x + y == 2020)
        .expect("No pair had a sum of 2020");

    println!("Part 1");
    dbg!(x, y);
    dbg!(x * y);

    let (x, y, z) = include_str!("input.txt")
        .lines()
        .map(str::parse::<i64>)
        .collect::<Result<Vec<_>, _>>()?
        .into_iter()
        .tuple_combinations::<(_, _, _)>()
        .find(|(x, y, z)| x + y + z == 2020)
        .expect("No triplet had a sum of 2020");

    println!("Part 2");
    dbg!(x, y, z);
    dbg!(x + y + z);
    dbg!(x * y * z);

    Ok(())
}
