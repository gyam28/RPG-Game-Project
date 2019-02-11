beginColor = "\x1b["
green = beginColor + "6;30;42m"
endColor = "\x1b[0m"
blue = beginColor + "0;30;44m"

def displayStatusBar (actualVal,maxVal, color):
    percentage = int(((actualVal *100) / maxVal) /10)
    bar = color
    if percentage == 0:
        bar = bar + endColor
    for i in range(10):
        bar = bar + " "
        if i == percentage-1:
            bar = bar + endColor
    return bar
