
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
      return data["length"];
    }

    //When passed a number n, this method will return the name of the nth key in the storage.
    async key(id) {
      console.debug(`${this.URL}/${this.TOKEN}/key/${id}`)
      const response = await fetch(`${this.URL}/${this.TOKEN}/key/${id}`);
      const data = await response.json();
      return data;
    }

    //When passed a key name, will return that key's value.
    async getItem(key) {
      console.debug(`${this.URL}/${this.TOKEN}/getItem`)
      const response = await fetch(`${this.URL}/${this.TOKEN}/getItem`,
      {method: 'POST', 
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "key": key,
        "data": "string"
      })});
      const data = await response.json();
      return data;
    }

    //When passed a key name and value, will add that key to the storage, or update that key's value if it already exists.
    async setItem(key, value) {
      console.debug(`${this.URL}/${this.TOKEN}/setItem`)
      const response = await fetch(`${this.URL}/${this.TOKEN}/setItem`,
      {method: 'POST', 
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "key": key,
        "data": value
      })});
      const data = await response.json();
      return data;
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
  



