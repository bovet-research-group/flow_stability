I think this would work the best: 
1. Set the network
--> check what would be the best way to compute the the transition matrix as a report on a small section of network, maybe highest and lowest density of the ingter laplacian  matrices
2. compute laplacians
3. For loop over scales: 
    then compute transition matrices in parallel
    compute the fs.set_flow_clustering() in parallel
    then clus_obj_for = fs.flow_clustering_backward[tau]
    save clus_obj_for.p1, clus_obj_for.I_list[0] #forward
    then  clus_obj_for = fs.flow_clustering_backward[tau]
    save clus_obj_for.p1, clus_obj_for.I_list[0] #forward


    also instead of saving one can do multiple louvain 
    and save the best resulgt of clustering 

