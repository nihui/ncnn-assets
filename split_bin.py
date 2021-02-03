import os
import glob
import argparse

def split(file, out_dir, split_size):
    _, filename = os.path.split(file)
    fsize = os.path.getsize(file)
    print(file, "size =", fsize)
    n = fsize // split_size
    if n > 99:
        print("spint parts > 99 not support now, please increase split size")
        return

    if n * split_size < fsize:
        n += 1
    print("split into", n, "parts size = ", split_size)
    with open(file, "rb") as fd_in:
        for i in range(n):
            print("part", i + 1)
            outfile = "%s.part%02d" %(os.path.join(out_dir, filename), i + 1)
            with open(outfile, "wb") as fd_out:
                fd_out.write(fd_in.read(split_size))
    print("split success")

def merge(in_file, out_file):
    files_in = glob.glob(in_file)
    with open(out_file, "wb") as fd_out:
        for file in files_in:
            with open(file, "rb") as fd_in:
                fd_out.write(fd_in.read())
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, help="file to split")
    parser.add_argument("--out-dir", type=str, default=".", help="out dir")
    parser.add_argument("--split-size", type=int, default=41943040, help="split the file into size")
    opt = parser.parse_args()

    split(opt.file, opt.out_dir, opt.split_size)
    # merge(opt.file + ".part*", opt.file)