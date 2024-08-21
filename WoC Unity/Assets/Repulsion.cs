using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Repulsion : MonoBehaviour
{
    public float G = 1.0f;
    public GameObject repeller;
    public GameObject target;

    List<List<float>> embeddings = new List<List<float>>();

    static float dotProduct;

     // Start is called before the first frame update
    void Start()
    {
        embeddings.Add(repeller.GetComponent<VideoProperties>().embedding);
        embeddings.Add(target.GetComponent<VideoProperties>().embedding);         
    }

    // Update is called once per frame
    void Update()
    {
        AddRepulsionForce(repeller, target, embeddings, G);
    }


    public static void AddRepulsionForce(GameObject repeller, GameObject target, List<List<float>> embeddings, float G)
    {
        // float dotProduct = repeller.mass*target.mass;
        for (int i=0; i < embeddings[0].Count; i++)
        {
            dotProduct = dotProduct + embeddings[0][i]*embeddings[1][0];
        }

        // float dotProduct = float.Dot(embeddings[0], embeddings[1]);



        //float distance = Vector3.Distance(repeller.position,target.position.
        Vector3 difference = repeller.GetComponent<Rigidbody>().position - target.GetComponent<Rigidbody>().position;
        float distance = difference.magnitude; // r = Mathf.Sqrt((x*x)+(y*y))

        // If the spheres are close together and attracted to each other, add the force
        if (distance <= 10.0f && dotProduct > 0)
        {
            //F = G * ((m1*m2)/r^2)
            // float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,2);
            float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,7);
            // float unScaledforceMagnitude = dotProduct/Mathf.Abs(Mathf.Log(distance));
            float forceMagnitude = G*unScaledforceMagnitude;

            Vector3 forceDirection = difference.normalized;

            Vector3 forceVector = forceDirection*forceMagnitude;

            target.GetComponent<Rigidbody>().AddForce(forceVector);
        }
        // Else if the spheres that are repelled (close and far away), add the force
        else if (dotProduct < 0)
        {
            //F = G * ((m1*m2)/r^2)
            float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,2);
            // float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,7);
            // float unScaledforceMagnitude = dotProduct/Mathf.Abs(Mathf.Log(distance));
            float forceMagnitude = G*unScaledforceMagnitude;

            Vector3 forceDirection = difference.normalized;

            Vector3 forceVector = forceDirection*forceMagnitude;

            target.GetComponent<Rigidbody>().AddForce(forceVector);
        }
        // Else the spheres are far away and attracted, do nothing

    }
}
