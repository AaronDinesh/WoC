using System.Collections;
using System.Collections.Generic;
using UnityEngine;

#if UNITY_EDITOR
using UnityEditor;
#endif


public class Replusion : MonoBehaviour
{
    public float G = 6.67f;

    public Rigidbody repeller;
    public Rigidbody target;
     // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        AddRepulsionForce(repeller, target, G);
    }


    public static void AddRepulsionForce(Rigidbody repeller, Rigidbody target, float G)
    {
        float massProduct = repeller.mass*target.mass;

        //You could also do
        //float distance = Vector3.Distance(repeller.position,target.position.
        Vector3 difference = repeller.position - target.position;
        float distance = difference.magnitude; // r = Mathf.Sqrt((x*x)+(y*y))

        //F = G * ((m1*m2)/r^2)
        float unScaledforceMagnitude = massProduct/Mathf.Pow(distance,2);
        float forceMagnitude = G*unScaledforceMagnitude;

        Vector3 forceDirection = difference.normalized;

        Vector3 forceVector = forceDirection*forceMagnitude;

        target.AddForce(-1*forceVector);
    }
}
