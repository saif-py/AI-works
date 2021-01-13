from subprocess import call


def func(listt):
    if listt[0].lower() == 'open':
        import os

        a = os.popen("""
        aptitude -F' * %p -> %d ' --no-gui --disable-columns search '?and(~i,!?section(libs), 
        !?section(kernel), !?section(devel))'
         """).readlines()
        for i in a:
            if i.__contains__(listt[1]):
                print(i)
                i = i.split()
                print("opening " + i[1])
                call(i[1])


listt = input().split()
func(listt)