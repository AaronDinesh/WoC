using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ArrowGenerator : MonoBehaviour
{
    Mesh mesh;
    
    [SerializeField]
    public List<Vector3> points;
    [SerializeField]
    public int[] triangles;





    // Start is called before the first frame update
    void Start()
    {
        // Create a new mesh and assign it to the MeshFilter Component
        mesh = new Mesh();
        this.GetComponent<MeshFilter>().mesh = mesh;        
        GenArrow(0.25f, 1.0f, 0.5f, 0.33f, new Vector3(0,0,0), new Vector3(1, 0, 0));
    }

    // Update is called once per frame
    void Update()
    {
        DrawArrow();        
    }

    void DrawArrow(){
        mesh.Clear();
        mesh.vertices = points.ToArray();
        mesh.triangles = triangles;
    }

    void GenArrow(float BodyWidth, float BodyHeight, float TipWidth, float TipHeight, Vector3 start, Vector3 end){
        //Left-Right is x (Right +ve). Up-Down is y (Up +ve). Forward-Backward is z (Forward +ve).
        //Starting arrow at the bottom left and going clockwise
        float theta = 0.0f;
        float rho = 0.0f;
        float gamma = 0.0f;

        //arrow is made in the xy plane. There needs to be some constant offset
        //to the angles below


        if(end.x - start.x != 0){ 
            //Angle between x and y axis. I.e. Rotation about Z axis
            theta = Mathf.Atan((end.y - start.y)/(end.x - start.x));
            //Angle between z and x. I.e. Rotation about the Y axis
            rho = Mathf.Atan((end.z - start.z)/(end.x - start.x));
        }
        
        if(end.y - start.y != 0){
            //Angle between z and y. I.e. Rotation about the X axis
            gamma = Mathf.Atan((end.z - start.z)/(end.y - start.y));
        }
        Vector3 eulerAngleRotation = new Vector3(gamma, rho, theta) * Mathf.Rad2Deg;
        Debug.Log(eulerAngleRotation);
        
        
        float zOffset = 0.1f;
        //Bottom left
        points.Add(new Vector3(start.x - BodyWidth/2, start.y, start.z));
        
        //Top left
        points.Add(new Vector3(start.x - BodyWidth/2, start.y + BodyHeight, start.z));
        
        //Top right
        points.Add(new Vector3(start.x + BodyWidth/2, start.y + BodyHeight, start.z));
        
        //Bottom right
        points.Add(new Vector3(start.x + BodyWidth/2, start.y, start.z));

        //Bottom left of tip
        points.Add(new Vector3(start.x - TipWidth/2, start.y + BodyHeight, start.z));

        //Bottom right of tip
        points.Add(new Vector3(start.x + TipWidth/2, start.y + BodyHeight, start.z));

        //Top of tip
        points.Add(new Vector3(start.x, start.y + BodyHeight + TipHeight, start.z));


        //Adding some depth
        //Bottom left
        points.Add(new Vector3(start.x - BodyWidth/2, start.y, start.z + zOffset));
        
        //Top left
        points.Add(new Vector3(start.x - BodyWidth/2, start.y + BodyHeight, start.z + zOffset));
        
        //Top right
        points.Add(new Vector3(start.x + BodyWidth/2, start.y + BodyHeight, start.z + zOffset));
        
        //Bottom right
        points.Add(new Vector3(start.x + BodyWidth/2, start.y, start.z + zOffset));

        //Bottom left of tip
        points.Add(new Vector3(start.x - TipWidth/2, start.y + BodyHeight, start.z + zOffset));

        //Bottom right of tip
        points.Add(new Vector3(start.x + TipWidth/2, start.y + BodyHeight, start.z + zOffset));

        //Top of tip
        points.Add(new Vector3(start.x, start.y + BodyHeight + TipHeight, start.z + zOffset));
        
        for(int i = 0; i < points.Count; i++){
            points[i] = Quaternion.Euler(eulerAngleRotation) * points[i];
        }
        
        
        triangles = new int[48] {0, 1, 2, 
                                2, 3, 0, 
                                4, 6, 5,
                                0, 7, 8,
                                8, 1, 0,
                                3, 2, 9,
                                9, 10,3,
                                6, 4,11,
                                11,13,6,
                                12,5, 6,
                                6,13,12,
                                10, 9,7,
                                9, 8, 7,
                                12,13,11,
                                4, 5, 12,
                                4, 12,11};
    }

}
