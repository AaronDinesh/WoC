using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovement : MonoBehaviour
{
    public float moveSpeed = 5f;
    public float smoothTime = 0.3f;
    public float mouseSensitivity = 2f;
    public float minVerticalAngle = -90f;
    public float maxVerticalAngle = 90f;

    private Vector3 velocity = Vector3.zero;
    private Vector3 targetPosition;
    private float rotationX = 0f;
    private float rotationY = 0f;

    void Start()
    {
        targetPosition = transform.position;
        //Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = true;
    }

    void Update()
    {
        HandleMovement();
        HandleRotation();
    }

    void HandleMovement()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");
        float upDownInput = 0f;

        if (Input.GetKey(KeyCode.Space))
        {
            upDownInput = 1f;
        }
        else if (Input.GetKey(KeyCode.LeftShift) || Input.GetKey(KeyCode.RightShift))
        {
            upDownInput = -1f;
        }

        Vector3 movement = transform.right * horizontalInput + transform.up * upDownInput + transform.forward * verticalInput;
        movement = movement.normalized;

        targetPosition += movement * moveSpeed * Time.deltaTime;
        transform.position = Vector3.SmoothDamp(transform.position, targetPosition, ref velocity, smoothTime);
    }

    void HandleRotation()
    {
        if (Input.GetMouseButton(1)) // Right mouse button
        {
            float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity;
            float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity;

            rotationY += mouseX;
            rotationX -= mouseY;
            rotationX = Mathf.Clamp(rotationX, minVerticalAngle, maxVerticalAngle);

            transform.localRotation = Quaternion.Euler(rotationX, rotationY, 0f);
        }
    }

    void OnDisable()
    {
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
    }



}
