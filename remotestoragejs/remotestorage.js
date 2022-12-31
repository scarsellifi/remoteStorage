
/**
 * Class remoteStorage.
 *
 * @class remoteStorage
 */
 export class RemoteStorage {

    constructor(url, token) {
      this.URL = `${url}`,
      this.TOKEN = token;
      this.length_int = null
    }
    // Returns an integer representing the number of data items stored in the Storage object.
    async length() {
      console.debug(`${this.URL}/${this.TOKEN}/length`)
      const response = await fetch(`${this.URL}/${this.TOKEN}/length`);
      const data = await response.json();
      return data;
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
  



