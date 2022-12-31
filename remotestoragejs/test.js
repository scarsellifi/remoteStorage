import { RemoteStorage } from './remotestorage.js';
import { assertEquals } from "https://deno.land/std@0.168.0/testing/asserts.ts";

Deno.test("RemoteStorage test", () => {
    const remotestorage = new RemoteStorage('http://0.0.0.0:8000','ABCDEFGHI');
    assertEquals(remotestorage.URL, "http://0.0.0.0:8000");
});

Deno.test("RemoteStorage length", async () => {
    const remotestorage = new RemoteStorage('http://0.0.0.0:8000','ABCDEFGHI');
    let result = await remotestorage.length()
    
    assertEquals(result, {
        "length": 1
      })

});