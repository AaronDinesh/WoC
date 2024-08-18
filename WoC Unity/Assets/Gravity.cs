using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Gravity : MonoBehaviour
{
    public static float G = 1.0f;

    public Rigidbody attractor;
    public Rigidbody target;

     // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        AddGravityForce(attractor, target);
    }


    public static void AddGravityForce(Rigidbody attractor, Rigidbody target)
    {
        float massProduct = attractor.mass*target.mass*G;

        //You could also do
        //float distance = Vector3.Distance(attractor.position,target.position.
        Vector3 difference = attractor.position - target.position;
        float distance = difference.magnitude; // r = Mathf.Sqrt((x*x)+(y*y))

        //F = G * ((m1*m2)/r^2)
        // float unScaledforceMagnitude = massProduct/Mathf.Pow(distance,2);

        float unScaledforceMagnitude = massProduct;
        float forceMagnitude = G*unScaledforceMagnitude;

        Vector3 forceDirection = difference.normalized;

        Vector3 forceVector = forceDirection*forceMagnitude;

        target.AddForce(forceVector);
    }
}
