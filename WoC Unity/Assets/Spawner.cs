using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using Newtonsoft.Json;

public class Spawner : MonoBehaviour
{
    public GameObject spherePrefab;
    GameObject[] gameObjects;


    // Start is called before the first frame update
    void Start()
    {
        // Path to the JSON file
        string path = Path.Combine(Application.streamingAssetsPath, "embeddings.json");

        // Load the JSON file
        string jsonString = File.ReadAllText(path);

        Dictionary<string, List<float>> embeddings = JsonConvert.DeserializeObject<Dictionary<string, List<float>>>(jsonString);
        var idEnumerator = embeddings.Keys.GetEnumerator();
        var embeddingEnumerator = embeddings.Values.GetEnumerator();
        
        
        foreach(KeyValuePair<string, List<float>> entry in embeddings){
            Vector3 spawnPos = new Vector3(entry.Value[0], entry.Value[1], entry.Value[2]);
            Instantiate(spherePrefab, spawnPos, Quaternion.identity);
        }
        
        // for (int i=0; i < embeddings.Count; i++)
        // {
        //     float x = Random.Range(-10.0f, 10.0f);
        //     float y = Random.Range(-10.0f, 10.0f);
        //     float z = Random.Range(-10.0f, 10.0f);
        //     Vector3 spawnPos = new Vector3(x, y, z);

        //     Instantiate(spherePrefab, spawnPos, Quaternion.identity);
        // }

        gameObjects=GameObject.FindObjectsOfType(typeof(GameObject)) as GameObject[];
        foreach(GameObject go in gameObjects)
        {
            // Loop through each Sphere
            if (go.name == "Sphere(Clone)")
            {
                
                //Gravity scriptGravity = go.AddComponent<Gravity>(); // Add gravity to center
                //scriptGravity.attractor = GameObject.Find("Center").GetComponent<Rigidbody>();
                //scriptGravity.target = go.GetComponent<Rigidbody>();
                VideoProperties scriptVideoProperties = go.AddComponent<VideoProperties>();
                
                idEnumerator.MoveNext();
                embeddingEnumerator.MoveNext();
                
                scriptVideoProperties.id = idEnumerator.Current;
                scriptVideoProperties.embedding = embeddingEnumerator.Current;
                Repulsion scriptRepulsion = go.AddComponent<Repulsion>();
                scriptRepulsion.repeller = go;

                // Loop through each other Sphere that isn't the current sphere
                foreach(GameObject gameObj in gameObjects)
                {
                    if (gameObj.name == "Sphere(Clone)" && gameObj != go)
                    {
                        scriptRepulsion.targets.Add(gameObj);
                    }
                }
            }
        }

    }

    // Update is called once per frame
    void Update()
    {

    }
}
