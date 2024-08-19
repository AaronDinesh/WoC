using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    public GameObject spherePrefab;
    GameObject[] gameObjects;


    // Start is called before the first frame update
    void Start()
    {
        for (int i=0; i < 100; i++)
        {
            float x = Random.Range(-40.0f, 40.0f);
            float y = Random.Range(-40.0f, 40.0f);
            float z = Random.Range(-40.0f, 40.0f);
            Vector3 spawnPos = new Vector3(x, y, z);

            Instantiate(spherePrefab, spawnPos, Quaternion.identity);
        }

        gameObjects=GameObject.FindObjectsOfType(typeof(GameObject)) as GameObject[];

        foreach(GameObject go in gameObjects)
        {
            // Loop through each Sphere
            if (go.name == "Sphere(Clone)")
            {
                Gravity scriptGravity = go.AddComponent<Gravity>(); // Add gravity to center
                scriptGravity.attractor = GameObject.Find("Center").GetComponent<Rigidbody>();
                scriptGravity.target = go.GetComponent<Rigidbody>();

                // Loop through each other Sphere that isn't the current sphere
                foreach(GameObject gameObj in gameObjects)
                {
                    if (gameObj.name == "Sphere(Clone)" && gameObj != go)
                    {
                        Repulsion scriptRepulsion = go.AddComponent<Repulsion>();
                        scriptRepulsion.repeller = gameObj.GetComponent<Rigidbody>();
                        scriptRepulsion.target = go.GetComponent<Rigidbody>();
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
