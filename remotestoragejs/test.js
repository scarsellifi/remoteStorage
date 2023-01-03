import { RemoteStorage } from './remotestoragedeno.js';
import { assertEquals } from "https://deno.land/std@0.168.0/testing/asserts.ts";

Deno.test("RemoteStorage test", () => {
    const remotestorage = new RemoteStorage('http://0.0.0.0:8000','ABCDEFGHI');
    assertEquals(remotestorage.URL, "http://0.0.0.0:8000");
});

Deno.test("RemoteStorage length", async () => {
    const remotestorage = new RemoteStorage('http://0.0.0.0:8000','ABCDEFGHI');
    let result = await remotestorage.length()
    console.log(result)
    assertEquals(result >= 1 , true)

});

Deno.test("RemoteStorage key", async () => {
    const remotestorage = new RemoteStorage('http://0.0.0.0:8000','ABCDEFGHI');
    let result = await remotestorage.key(0)
    console.log(result)
    assertEquals(result, {
        "data": "content\n ",
        "key": "key"
      })

});

Deno.test("RemoteStorage getItem", async () => {
    const remotestorage = new RemoteStorage('http://0.0.0.0:8000','ABCDEFGHI');
    let result = await remotestorage.getItem("key")
    console.log(result)
    assertEquals(result, {
        "data": "content\n ",
        "key": "key"
      })

});

Deno.test("RemoteStorage setItem", async () => {
    const remotestorage = new RemoteStorage('http://0.0.0.0:8000','ABCDEFGHI');
    let result = await remotestorage.setItem("key6", "content\n ")
    console.log(result)
    assertEquals(result, {
        "data": "content\n ",
        "key": "key6"
      })

});