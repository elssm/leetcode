int romanToInt(char* s) {
    char *p = s;
    int total=0, before=0, after=0;
    while(*p != '\0')
    {
        switch(*p)
        {
            case 'I':after = 1;break;
            case 'V':after = 5;break;
            case 'X':after = 10;break;
            case 'L':after = 50;break;
            case 'C':after = 100;break;
            case 'D':after = 500;break;
            case 'M':after = 1000;break;
        }
        if(after > before)
            total = total + (after - 2*before);
        else
            total += after;
        before = after;
        p++;
    }
    return total;
}
