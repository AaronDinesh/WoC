using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Replusion : MonoBehaviour
{
    public static float G = 6.0f;

    public Rigidbody repeller;
    public Rigidbody target;

     // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        AddRepulsionForce(repeller, target);
    }


    public static void AddRepulsionForce(Rigidbody repeller, Rigidbody target)
    {
        float massProduct = repeller.mass*target.mass*G;

        //You could also do
        //float distance = Vector3.Distance(repeller.position,target.position.
        Vector3 difference = repeller.position - target.position;
        float distance = difference.magnitude; // r = Mathf.Sqrt((x*x)+(y*y))

        //F = G * ((m1*m2)/r^2)
        float unScaledforceMagnitude = massProduct/Mathf.Pow(distance,1);
        float forceMagnitude = G*unScaledforceMagnitude;

        Vector3 forceDirection = difference.normalized;

        Vector3 forceVector = forceDirection*forceMagnitude;

        target.AddForce(-1*forceVector);
    }
}
