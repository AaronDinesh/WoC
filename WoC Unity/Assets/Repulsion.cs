using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Repulsion : MonoBehaviour
{
    public float G = 10.0f;
    public GameObject repeller;
    public List<GameObject> targets = new List<GameObject>();
    public List<float> dotProducts = new List<float>();

    List<float> repellerEmbedding;

    // Start is called before the first frame update
    void Start()
    {
        repellerEmbedding = repeller.GetComponent<VideoProperties>().embedding;
        
        foreach(GameObject target in targets){
            float dotProduct = 0.0f;
            List<float> targetEmbedding = target.GetComponent<VideoProperties>().embedding;
             // float dotProduct = repeller.mass*target.mass;
            for(int i = 0; i < repellerEmbedding.Count; i++){
                dotProduct += repellerEmbedding[i] * targetEmbedding[i];
            }
            dotProducts.Add(dotProduct);
        }
    }

    void ColorTargets(){
        
        
        for(int i = 0; i < targets.Count; i++){
            MeshRenderer meshRendererTarget = targets[i].GetComponent<MeshRenderer>();
            Material newMaterialTarget = new Material(Shader.Find("Standard"));
        


            if(dotProducts[i] > 0){
                newMaterialTarget.color = new Color(0, 255, 0, 1);
                meshRendererTarget.material = newMaterialTarget;
            }else if(dotProducts[i] < 0){
                newMaterialTarget.color = new Color(255, 0, 0, 1);
                meshRendererTarget.material = newMaterialTarget;
            }
        }
    }


    // Update is called once per frame
    void Update()
    {
        //AddRepulsionForce(repeller, target, embeddings, dotProduct, G);

        // float dotProduct = repeller.mass*target.mass;
        // for (int i=0; i < embeddings[0].Count; i++)
        // {
        //     dotProduct = dotProduct + 100*embeddings[0][i]*embeddings[1][0];
        // }

        // float dotProduct = float.Dot(embeddings[0], embeddings[1]);

        //float distance = Vector3.Distance(repeller.position,target.position.

        float forceMagnitude = 0.0f;
        Vector3 forceDirection = new Vector3(0.0f, 0.0f, 0.0f);
        for(int i = 0; i < targets.Count; i++){
            Vector3 difference = repeller.GetComponent<Rigidbody>().position - targets[i].GetComponent<Rigidbody>().position;
            forceDirection += difference.normalized;
            float distance = difference.magnitude;

            if(distance <= 200.0f && dotProducts[i] > 0){
                forceMagnitude += (G*dotProducts[i])/Mathf.Pow(distance, 2);
            }else if(dotProducts[i] < 0){
                forceMagnitude += (G*dotProducts[i])/Mathf.Pow(distance, 1);
            }
        }

        Vector3 forceVector = forceMagnitude * forceDirection;
        repeller.GetComponent<Rigidbody>().AddForce(forceVector);

        
        // Vector3 difference = repeller.GetComponent<Rigidbody>().position - target.GetComponent<Rigidbody>().position;
        // float distance = difference.magnitude; // r = Mathf.Sqrt((x*x)+(y*y))

        // // If the spheres are close together and attracted to each other, add the force
        // if (distance <= 200.0f && dotProduct > 0)
        // {
        //     //F = G * ((m1*m2)/r^2)
        //     // float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,2);
        //     float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,2);
        //     // float unScaledforceMagnitude = dotProduct/Mathf.Abs(Mathf.Log(distance));
        //     float forceMagnitude = G*unScaledforceMagnitude;

        //     Vector3 forceDirection = difference.normalized;

        //     Vector3 forceVector = forceDirection*forceMagnitude;

        //     target.GetComponent<Rigidbody>().AddForce(forceVector);
        // }
        // // Else if the spheres that are repelled (close and far away), add the force
        // else if (dotProduct < 0)
        // {
        //     //F = G * ((m1*m2)/r^2)
        //     float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,2);
        //     // float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,7);
        //     // float unScaledforceMagnitude = dotProduct/Mathf.Abs(Mathf.Log(distance));
        //     float forceMagnitude = G*unScaledforceMagnitude;

        //     Vector3 forceDirection = difference.normalized;

        //     Vector3 forceVector = forceDirection*forceMagnitude;

        //     target.GetComponent<Rigidbody>().AddForce(forceVector);
        // }
        // // Else the spheres are far away and attracted, do nothing

        // dotProduct = 0;
        
        if (Input.GetMouseButtonDown(0)) // Left mouse button
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            
            if (Physics.Raycast(ray, out hit))
            {
                // Your code here
                Debug.Log("Clicked on: " + hit.collider.gameObject.name);
                
                MeshRenderer meshRendererRepeller = hit.collider.gameObject.GetComponent<MeshRenderer>();
                Material newMaterialRepeller = new Material(Shader.Find("Standard"));
                newMaterialRepeller.color = new Color(255, 255, 0, 1);
                meshRendererRepeller.material = newMaterialRepeller;

                
                
                
                ColorTargets();
            }
        }



    }


    // public static void AddRepulsionForce(GameObject repeller, GameObject target, List<List<float>> embeddings, float dotProduct, float G)
    // {
    //     // float dotProduct = repeller.mass*target.mass;
    //     for (int i=0; i < embeddings[0].Count; i++)
    //     {
    //         dotProduct = dotProduct + 100*embeddings[0][i]*embeddings[1][0];
    //     }

    //     // float dotProduct = float.Dot(embeddings[0], embeddings[1]);



    //     //float distance = Vector3.Distance(repeller.position,target.position.
    //     Vector3 difference = repeller.GetComponent<Rigidbody>().position - target.GetComponent<Rigidbody>().position;
    //     float distance = difference.magnitude; // r = Mathf.Sqrt((x*x)+(y*y))

    //     // If the spheres are close together and attracted to each other, add the force
    //     if (distance <= 200.0f && dotProduct > 0)
    //     {
    //         //F = G * ((m1*m2)/r^2)
    //         // float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,2);
    //         float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,2);
    //         // float unScaledforceMagnitude = dotProduct/Mathf.Abs(Mathf.Log(distance));
    //         float forceMagnitude = G*unScaledforceMagnitude;

    //         Vector3 forceDirection = difference.normalized;

    //         Vector3 forceVector = forceDirection*forceMagnitude;

    //         target.GetComponent<Rigidbody>().AddForce(forceVector);
    //     }
    //     // Else if the spheres that are repelled (close and far away), add the force
    //     else if (dotProduct < 0)
    //     {
    //         //F = G * ((m1*m2)/r^2)
    //         float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,1);
    //         // float unScaledforceMagnitude = dotProduct/Mathf.Pow(distance,7);
    //         // float unScaledforceMagnitude = dotProduct/Mathf.Abs(Mathf.Log(distance));
    //         float forceMagnitude = G*unScaledforceMagnitude;

    //         Vector3 forceDirection = difference.normalized;

    //         Vector3 forceVector = forceDirection*forceMagnitude;

    //         target.GetComponent<Rigidbody>().AddForce(forceVector);
    //     }
    //     // Else the spheres are far away and attracted, do nothing

    // }
}
