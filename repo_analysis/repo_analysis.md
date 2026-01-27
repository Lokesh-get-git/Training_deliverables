## scientificcalc.py - Repository Analysis
### 1. Overview
A 15k-char single-file Tkinter scientific calculator with basic arithmetic (+−×÷) and 20+ advanced functions (trig, logs, hyperbolics, constants). Supports two modes: compact Standard (480px) and expanded Scientific (944px). Event-driven state machine handles calculator logic.

### 2. Code Structure
text
scientificcalc.py
├── Imports: tkinter.*, math  
├── GUI Setup: root → calc Frame → txtDisplay Entry
├── class Calc()
│   ├── State vars: total, current, input_value, check_sum, op, result
│   ├── Core methods: numberEnter(), operation(), sum_of_total()  
│   └── 20+ Math methods: sin/cos/tan/π/e/log/exp/√/lgamma
├── Button grid: 30+ buttons (numbers + ops + scientific)
└── Menu: Toggle Standard ↔ Scientific layouts
Key Design: Single Calc() instance (added_value) manages all state. Global txtDisplay Entry shows current value.

### 3. Execution Flow
text
1. Startup → display="0", Calc() initialized
2. DIGIT → numberEnter(num) → self.current += str(num) → display
3. OP(+−×÷) → operation(op) → store total/current → set flags  
4. = → sum_of_total() → valid_function() → total OP current → reset
5. UNARY(sin/√/log) → math.func(display) → direct display override
6. C → clear current | CE → clear total+current
State Machine: input_value (new number?), check_sum (op pending?), result (post-equals)

### 4. Performance Bottlenecks
Issue	Problem	Fix
1. Lambda Overload	30+ lambdas recreated every mode switch	functools.partial(method, arg)
2. Float Parse Spam	float(current) on every op/unary	Store string, parse only at =
3. String Concat	current += num → quadratic time	current_list.append() + ''.join()
4. Display Thrash	2-3 delete(0,END) per click	Dirty flag → batch updates
5. Global Coupling	txtDisplay global → untestable	self.display_widget in __init__

diagram_url: https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&dark=auto#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%22PWdzeC_ESjIcf68S-qAC%22%3E7Vxbc%2BI4Fv4t80BV8gAl%2Be7HQELvXHqmq9Ozu%2F2UUmwB2hiLkUUS5tfv0cVgAaGTgDNJlVNUkI7kY%2FnoO5%2BOLqbnj%2BaPnwRZzD7znBY9D%2BWPPf%2By53lxGMN%2FJVgZQRpgI5gKlhsR2giu2d%2FUCHEtXbKcVlZmRJLzQrKFK8x4WdJMOjIiBH9wq014kTuCBZlSpxlKcJ2Rgu5U%2Bw%2FL5cxIk7BR%2B1%2BUTWf1nTGyJXNSV7aCakZy%2FtAQ%2BVc9fyQ4lyY1fxzRQtnOtcv4idJ1wwQt5XMu%2BPvX73%2BNVv%2F%2B381iWYjlbfarl%2F7Sx675yG2xbY2Nelu1kqu60lTw5cJI70mxtFIroELSx8aVtlWfKJ9TKVZQZdYwXIATc93Dxsp%2BFAwQ8n0%2F8EMUJmHqmypWa2CzFllhYHvd9vh0faONUSBh7fICG4W7pjhoy4aBwD5lTpVy1POHDzMm6fWCZKr0AdwFZDM5h8ZcYkieyJB%2BumNInMau5RzD9df%2BcmrL1U5M8%2Bm2Oz3XlnwpMvrjzmnYnJb5hXJ8yJW8pK6N3Q6Z8FJaysFg12EliagFCeRBVSOXLcW9vlQpoo9M%2FhfSfQQQ9azgu9I7wH5s85eP9kY6s2pkvlDBwMZU1LIS7K304VqdEtT60lqwUahzq2ZuW6UlSyKm9JClw72wO4yxmv0ELYhk927fNnBX19sHLHuHL5wBENbIxL7nYBMHiavCAMJe1WS7bUWJqyjd0mPssqNHw3z91Ecg33s9aYC3Sxe1%2B4ijkoLf0REvuNggfcKKYktECjYtIVvQidKq2ITB8HZhxXOW5%2BrGW56xAwo2X3Ahq54XFUpNzu4hOVVJGKFV%2B%2B9oQSUv6wpgtUad1zGZtwOoxB0BcOT0cXAAbkfxWPShRgAc7Q6lOHZHgJqZa%2B9obQTw35sfZNAOxZGv9oSsIFWlQiZSZGfnr%2BohH%2B10UOz9M%2F0TfCxoe%2BEutOtYdT8p4PaimyMCQ4vtU5N4BfZn5fQ3Xe0y2Ei%2BWhsqEYfLJ4UOkGZwIQUNw4UaCLWBwiF8wKIjNAh7IbR1BHm8ycNHVRdyxEtoPmH60Smp5AOtpHYfSeqJxGuAAUGYpFokqlN5V%2BJCxHNnDthva%2BDAR4wcHUSehEjGhUII9NGM56cDSXQQJFFrIIk7kLQAks9qAebkIMHIO4iSNGoLJUmHkhZQcruUMGtR8Zzq7NdNVJ4Bk614zktaC0rSDiYtwKRczm9h1qDsmsP%2FgvPFG0HFx21BZd8abweV4xmFVCwDEV8oVjlTfTO6Otk88Udo8cOW0OIfMVPs0PL0bCdjYE422UDmRDip99mewEnUFqv43ay4DZzMablUdFJJGH%2FGgBoV2vKcno5YfgCYOGkJMMHxw9DL157MIjXAoHQURn8t1XbsMDNAu4BCMb09U4un8HBo%2FR2da7VIbSD1J2TOipWpDUGCWghffeYlN3WXrD%2BHTKVbpyXXY1Xa%2F0qny4III9tU2eit9NaT0oqDxWOzwLRXlZRczEnRKLsnghH4Bh8gcinU1vnBehlZPFXlwQJGFQbIrIWigkpJRd860O6VXCxmpLQqPSNTvdS3zqpNavSui1iZ655XZah%2BUl0CnlRWE1Bf36i0BgLg6q39xl0euMjddq11waPc3jFQp3Qadulb6Dv1NI76th9UyUJARYMn1bkku5vqVc9%2BAyD8rshmZ2gQJWqPCaEB8mLVZygdhMCFSHmHEuPzxoPlNOOCSMbLvpyx7K6klX0aVjLJamtu1230%2FMF6jeY59XJWLQqyqksKVqp1lJ%2FM5g4pbacADRK5ZfHaM%2BodnYqB54wzDgPWuOBT9ZCjcU%2Bts42pylx5vSTppUrHmbLB8LyxM2T87oitoT173B4K3Yk5wvrwQBCFYRzhen19PU%2FHgxBKcejFMUpbm7XvmbR%2FmI2OTWhyo%2FY6BovVqcaayF2OxRg6w%2Bme1s5y%2BHsWZLthpRtWumHlfQwr%2BjgcPJwaPqJeqhxMcQ98jQWZ060i%2BSgv7a1bHlzC1B1cgmSQwl%2FshX6A47TecV8fcoTSKIKBJYFKyGuNzfbsHHRs1rFZx2bvg80adIWU%2F%2BcQbd0YF1OaK9Cm8P62cbEXaupKgjjAMMtP3cOgOPDeiLteEhp33NVxV8ddb81dkkvQq%2BGbLYV2U52ZFGRatUxb20fWvQAfpK04HQRvQlt79lc72upoq6Otd0NbZq%2F%2BSq9%2BaRDzBTX3N1njUa3GXF6yRV77X2SqT4NgU9z2YmS9w9NxV8ddHXe9Q%2B6CuSLENQlyEvViV0HmtznpuStg5nRjT6%2BSFW3HZN7WSXsviDVveQmkUIxcVvN95IZkbbGa94H3WC5EppqRKVrRWCJTQean2mfBoTsORe4uS99rrU%2F2vPbzYfpEnwJpvS9i9FadEb6Xd7z9ePcVUd93OSWu3Xl97L4tqzz32Em4a5N%2F5KW%2B3Tef%2FC3GxfXh39P783MP%2F%2B0x1oF4csc0198uvn6DYavn%2Bdj45iY58noXqDH8%2BYfq1dtCzQAUNUdcc9gbjexLfM%2B9I%2BqFw6E%2BMq4uLiDK0KfB9l6%2BT5ObuPz508%2Ffev74qXJ7bxUKeOuY4PvV9Z5AwZn2nG2eNN4kz5%2FRolcm1o180SU7vfhE3T9%2Fv%2Fj6%2FVRm2jm44sRTORPqV0Q2Ud0HNRkk%2FvjyA5O93HbrifRZ05WGDsQcc1bSvKllVxI%2FrC1tAtjk1CatlvMbPrmxBnKMB7zI8pvJsszM2sWHtZ45An8qBx4VlIibq1KPa2OY9txkWkKN5CX8%2B8wnO6Toz0VuXle9PIYwXnpXmwiHV%2Fd6VR79pl5ICS9PH5a9IJSA7ObXjMwPaWx%2BEsq%2F%2Bj8%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E
