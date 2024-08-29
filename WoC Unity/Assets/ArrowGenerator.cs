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
        GenArrowBody(3.0f,4.0f);
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

    void GenArrowBody(float width, float height){
        //Bottom center of the arrow body will be at (0, 0, 0)
        //Left-Right is x (Right +ve). Up-Down is y (Up +ve). Forward-Backward is z (Forward +ve).
        //Starting arrow at the bottom left and going clockwise
        
        //Bottom left
        points.Add(new Vector3(-width/2, 0, 0));
        
        //Top left
        points.Add(new Vector3(-width/2, height, 0));
        
        //Top right
        points.Add(new Vector3(width/2, height, 0));
        
        //Bottom right
        points.Add(new Vector3(width/2, 0, 0));
        
        triangles = new int[6] {0, 1, 2, 2, 3, 0};

    }

}
