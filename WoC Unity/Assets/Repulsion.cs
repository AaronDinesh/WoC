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

        //F = G * ((m1*m2)/r^2)
        float unScaledforceMagnitude = massProduct/Mathf.Pow(distance,2);
        float forceMagnitude = G*unScaledforceMagnitude;

        Vector3 forceDirection = difference.normalized;

        Vector3 forceVector = forceDirection*forceMagnitude;

        target.AddForce(forceVector);
    }
}
