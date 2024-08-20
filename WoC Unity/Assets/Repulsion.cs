using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Repulsion : MonoBehaviour
{
    public float G = 1.0f;
    public Rigidbody repeller;
    public Rigidbody target;

    List<Vector3> embeddings = new List<Vector3>();

     // Start is called before the first frame update
    void Start()
    {
        embeddings.Add(repeller.position);
        embeddings.Add(target.position);         
    }

    // Update is called once per frame
    void Update()
    {
        AddRepulsionForce(repeller, target, embeddings, G);
    }


    public static void AddRepulsionForce(Rigidbody repeller, Rigidbody target, List<Vector3> embeddings, float G)
    {
        // float massProduct = repeller.mass*target.mass;
        float massProduct = Vector3.Dot(embeddings[0], embeddings[1]);


        //float distance = Vector3.Distance(repeller.position,target.position.
        Vector3 difference = repeller.position - target.position;
        float distance = difference.magnitude; // r = Mathf.Sqrt((x*x)+(y*y))

        // If the spheres are close together and attracted to each other, add the force
        if (distance <= 10.0f && massProduct > 0)
        {
            //F = G * ((m1*m2)/r^2)
            // float unScaledforceMagnitude = massProduct/Mathf.Pow(distance,2);
            float unScaledforceMagnitude = massProduct/Mathf.Pow(distance,7);
            // float unScaledforceMagnitude = massProduct/Mathf.Abs(Mathf.Log(distance));
            float forceMagnitude = G*unScaledforceMagnitude;

            Vector3 forceDirection = difference.normalized;

            Vector3 forceVector = forceDirection*forceMagnitude;

            target.AddForce(forceVector);
        }
        // Else if the spheres that are repelled (close and far away), add the force
        else if (massProduct < 0)
        {
            //F = G * ((m1*m2)/r^2)
            float unScaledforceMagnitude = massProduct/Mathf.Pow(distance,2);
            // float unScaledforceMagnitude = massProduct/Mathf.Pow(distance,7);
            // float unScaledforceMagnitude = massProduct/Mathf.Abs(Mathf.Log(distance));
            float forceMagnitude = G*unScaledforceMagnitude;

            Vector3 forceDirection = difference.normalized;

            Vector3 forceVector = forceDirection*forceMagnitude;

            target.AddForce(forceVector);
        }
        // Else the spheres are far away and attracted, do nothing

    }
}
