from datetime import datetime
from hashlib import blake2b
import os


def getRandomSlug(slug, userID):

    now = datetime.now()
    currentTime = now.strftime("%Y-%m-%d %H:%M:%S")

    salt = os.urandom(blake2b.SALT_SIZE)
    hashFunction = blake2b(salt=salt)

    hashFunction.update(slug.encode("utf-8"))
    hashFunction.update(userID.encode("utf-8"))
    hashFunction.update(currentTime.encode("utf-8"))

    mainHashValue = hashFunction.hexdigest().encode("utf-8")

    shortHash = blake2b(mainHashValue, digest_size=6).hexdigest()

    newSlug = f"{slug}-{shortHash}"

    return newSlug