
/**
 * Class remoteStorage.
 *
 * @class remoteStorage
 */
 class RemoteStorage {

    constructor(url, token) {
      URL = `https://${url}`,
      TOKEN = token;
    }
    // Returns an integer representing the number of data items stored in the Storage object.
    length() {
      // todo
    }

    //When passed a number n, this method will return the name of the nth key in the storage.
    key(id) {
      // todo
    }

    //When passed a key name, will return that key's value.
    getItem(key) {
      // todo
    }

    //When passed a key name and value, will add that key to the storage, or update that key's value if it already exists.
    setItem(key, value) {
      // todo
    }


    //When passed a key name, will remove that key from the storage.
    removeItem(key) {
      // todo
    }


    //When invoked, will empty all keys out of the storage.
    clear() {
      // todo
    }
  
  }
  



