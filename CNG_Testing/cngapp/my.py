def formview(request):
    if request.method == 'POST':
        form = CngForm(request.POST or None)
        # if form.is_valid():
        vahicle_no = request.POST.get('vahicle_no')
        cylinder_weight = request.POST.get('cylinder_weight')
        vahicle_name = request.POST.get('vahicle_name')
        print(vahicle_no,vahicle_name,cylinder_weight)
        if form.is_valid():
            cngmodel = Cngmodel(vahicle_no=vahicle_no,cylinder_weight=cylinder_weight,vahicle_name=vahicle_name)
            cngmodel.save()
            print("succesful")
        # else:
        #     print(form.errors)
        # return redirect(request,"index.html")

    return render(request,"form.html")  


# def formview(request):
#     form = CngForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = CngForm()
#     context = {
#         'form':form
#     } 

#     return render(request,"form.html",context)     