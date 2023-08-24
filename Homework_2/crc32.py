import zlib

def crc32(fileName):
    # сумма файла
    with open(fileName, 'rb') as fh:
        hash = 0
        while True:
            s = fh.read(77852)
            if not s:
                break
            hash = zlib.crc32(s, hash)

        return "%08X" % (hash & 0xFFFFFFFF)