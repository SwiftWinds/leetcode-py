use std::io::{self, BufRead};
use std::collections::HashSet;

fn main() {
    let stdin = io::stdin();
    let mut total = 0;

    for line in stdin.lock().lines() {
        let line = line.expect("Failed to read line");
        let mid = line.len() / 2;
        let first: HashSet<char> = line[..mid].chars().collect();
        let second: HashSet<char> = line[mid..].chars().collect();

        let common = first.intersection(&second).next().expect("No common item found");

        total += if common.is_lowercase() {
            *common as u32 - 'a' as u32 + 1
        } else {
            *common as u32 - 'A' as u32 + 27
        };
    }

    println!("{}", total);
}