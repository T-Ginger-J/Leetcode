function countAndSay(n: number): string {
    let s = "1";

    for (let i = 1; i < n; i++) {
        let res: string[] = [];
        let prev = s[0];
        let count = 1;

        for (let j = 1; j < s.length; j++) {
            if (s[j] === prev) {
                count++;
            } else {
                res.push(count.toString(), prev);
                prev = s[j];
                count = 1;
            }
        }

        res.push(count.toString(), prev);
        s = res.join("");
    }

    return s;
}
